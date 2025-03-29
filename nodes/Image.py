import sys

class MC_SetTileSize:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "widthDiv": ("FLOAT", {"default": 1,
                   "min": -sys.float_info.max,
                   "max": sys.float_info.max,
                   "step": 0.01}),
                "heightDiv": ("FLOAT", {"default": 1,
                   "min": -sys.float_info.max,
                   "max": sys.float_info.max,
                   "step": 0.01}),
            }
        }

    RETURN_TYPES = ("INT", "INT",)
    RETURN_NAMES = ("tile_Width", "tile_Height")

    FUNCTION = 'set_tile_size'
    CATEGORY = "ComfyMC/Image"

    def set_tile_size(self, image, widthDiv, heightDiv):
        #size = get_image_size(image)
        new_width = int(image.shape[2] / widthDiv) if widthDiv != 0 else image.shape[2]
        new_height = int(image.shape[1] / heightDiv) if heightDiv != 0 else image.shape[1]
        return new_width, new_height
