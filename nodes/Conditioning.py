
import torch
from nodes import MAX_RESOLUTION

class MC_MultiConditioningConcat:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "clip": ("CLIP", ),
            "text1": ("STRING", {"multiline": True, "dynamicPrompts": True, "default": ""}),
            "text2": ("STRING", {"multiline": True, "dynamicPrompts": True, "default": ""}),
            "width": ("INT", {"default": 1024, "min": 0, "max": MAX_RESOLUTION}),
            "height": ("INT", {"default": 1024, "min": 0, "max": MAX_RESOLUTION}),
            "size_cond_factor": ("INT", {"default": 1, "min": 1, "max": 4}),
            "Type": ("INT", {"default": 1, "min": 1, "max": 5}),
        }}
    
    RETURN_TYPES = ("CONDITIONING","INT")
    RETURN_NAMES = ("OUT","Cond-Factor")
    FUNCTION = "switch"
    CATEGORY = "ComfyMC/Conditioning"
    DESCRIPTION = """Concat text1+text2 in the following fashion:
Type: 1 Codition text1 and text2 and then Condconcat1+Condconcat2.
Type: 2 Codition text2 and text1 and then Condconcat2+Condconcat1.
Type: 3 Textconcat text1+text2 and then Codition as a single prompt.
Type: 4 Textconcat text2+text1 and then Codition as a single prompt.
Type: 5 Codition text1.
"""
    def execute(self, clip, width, height, size_cond_factor, text):
        crop_w = 0
        crop_h = 0
        width = width*size_cond_factor
        height = height*size_cond_factor
        target_width = width
        target_height = height
        text_g = text_l = text

        tokens = clip.tokenize(text_g)
        tokens["l"] = clip.tokenize(text_l)["l"]
        if len(tokens["l"]) != len(tokens["g"]):
            empty = clip.tokenize("")
            while len(tokens["l"]) < len(tokens["g"]):
                tokens["l"] += empty["l"]
            while len(tokens["l"]) > len(tokens["g"]):
                tokens["g"] += empty["g"]
        cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)
        return ([[cond, {"pooled_output": pooled, "width": width, "height": height, "crop_w": crop_w, "crop_h": crop_h, "target_width": target_width, "target_height": target_height}]], )

    def condconcat(self, conditioning_to, conditioning_from):
        out = []

        if not conditioning_from or not conditioning_to:
            return conditioning_to

        # Ensure we are extracting the right elements
        cond_from = conditioning_from[0][0]  # Extract Tensor
        if not isinstance(cond_from, torch.Tensor):
            raise TypeError(f"Expected torch.Tensor but got {type(cond_from)}")

        for cond_item in conditioning_to:
            t1 = cond_item[0]  # Extract Tensor
            if not isinstance(t1, torch.Tensor):
                raise TypeError(f"Expected torch.Tensor but got {type(t1)}")

            tw = torch.cat((t1, cond_from), dim=1)  # Concatenate
            n = [tw, cond_item[1].copy()]  # Copy metadata
            out.append(n)

        return (out,)

    
    def switch(self, clip, Type, width, height, size_cond_factor, text1, text2):
        CondFactor = size_cond_factor
        
        cond1 = self.execute(clip, width, height, size_cond_factor, text1)[0]  # Extract first element
        cond2 = self.execute(clip, width, height, size_cond_factor, text2)[0]  # Extract first element

        if Type == 1:
            return (self.condconcat(cond1, cond2)[0],CondFactor)
        elif Type == 2:
            return (self.condconcat(cond2, cond1)[0],CondFactor)
        elif Type == 3:
            return (self.execute(clip, width, height, size_cond_factor, text1 + ", " + text2)[0],CondFactor)
        elif Type == 4:
            return (self.execute(clip, width, height, size_cond_factor, text2 + ", " + text1)[0],CondFactor)
        else:
            return (self.execute(clip, width, height, size_cond_factor, text1)[0],CondFactor)

class MC_MultiConditioningConcatAdvanced:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            "clip": ("CLIP", ),
            "text1": ("STRING", {"multiline": True, "dynamicPrompts": True, "default": ""}),
            "text2": ("STRING", {"multiline": True, "dynamicPrompts": True, "default": ""}),
            "size_cond_factor": ("INT", {"default": 1, "min": 1, "max": 4}),
            "Type": ("INT", {"default": 1, "min": 1, "max": 5}),
        },
        "optional": {
            "image": ("IMAGE",),
            "width": ("INT", {"default": 1024, "min": 0, "max": MAX_RESOLUTION}),
            "height": ("INT", {"default": 1024, "min": 0, "max": MAX_RESOLUTION}),
            }
        }
    
    RETURN_TYPES = ("CONDITIONING","CONDITIONING","CONDITIONING","INT")
    RETURN_NAMES = ("OUT","PROMPT","Q/A-TAGS","Cond-Factor")
    FUNCTION = "switch"
    CATEGORY = "ComfyMC/Conditioning"
    DESCRIPTION = """Concat text1+text2 in the following fashion:
Type: 1 Codition text1 and text2 and then Condconcat1+Condconcat2.
Type: 2 Codition text2 and text1 and then Condconcat2+Condconcat1.
Type: 3 Textconcat text1+text2 and then Codition as a single prompt.
Type: 4 Textconcat text2+text1 and then Codition as a single prompt.
Type: 5 Codition text1.
"""
    def execute(self, clip, width, height, size_cond_factor, text):
        crop_w = 0
        crop_h = 0
        width = width*size_cond_factor
        height = height*size_cond_factor
        target_width = width
        target_height = height
        text_g = text_l = text

        tokens = clip.tokenize(text_g)
        tokens["l"] = clip.tokenize(text_l)["l"]
        if len(tokens["l"]) != len(tokens["g"]):
            empty = clip.tokenize("")
            while len(tokens["l"]) < len(tokens["g"]):
                tokens["l"] += empty["l"]
            while len(tokens["l"]) > len(tokens["g"]):
                tokens["g"] += empty["g"]
        cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)
        return ([[cond, {"pooled_output": pooled, "width": width, "height": height, "crop_w": crop_w, "crop_h": crop_h, "target_width": target_width, "target_height": target_height}]], )

    def condconcat(self, conditioning_to, conditioning_from):
        out = []

        if not conditioning_from or not conditioning_to:
            return conditioning_to

        # Ensure we are extracting the right elements
        cond_from = conditioning_from[0][0]  # Extract Tensor
        if not isinstance(cond_from, torch.Tensor):
            raise TypeError(f"Expected torch.Tensor but got {type(cond_from)}")

        for cond_item in conditioning_to:
            t1 = cond_item[0]  # Extract Tensor
            if not isinstance(t1, torch.Tensor):
                raise TypeError(f"Expected torch.Tensor but got {type(t1)}")

            tw = torch.cat((t1, cond_from), dim=1)  # Concatenate
            n = [tw, cond_item[1].copy()]  # Copy metadata
            out.append(n)

        return (out,)

    
    def switch(self, clip, Type, width, height, size_cond_factor, text1, text2, image=None):
        CondFactor = size_cond_factor
        if image is not None:
            width = image.shape[2]
            height = image.shape[1]

        cond1 = self.execute(clip, width, height, size_cond_factor, text1)[0]  # Extract first element
        cond2 = self.execute(clip, width, height, size_cond_factor, text2)[0]  # Extract first element
    
        if Type == 1:
            return (self.condconcat(cond1, cond2)[0],cond1,cond2,CondFactor)
        elif Type == 2:
            return (self.condconcat(cond2, cond1)[0],cond1,cond2,CondFactor)
        elif Type == 3:
            return (self.execute(clip, width, height, size_cond_factor, text1 + ", " + text2)[0],cond1,cond2,CondFactor)
        elif Type == 4:
            return (self.execute(clip, width, height, size_cond_factor, text2 + ", " + text1)[0],cond1,cond2,CondFactor)
        else:
            return (self.execute(clip, width, height, size_cond_factor, text1)[0],cond1,cond2,CondFactor)

