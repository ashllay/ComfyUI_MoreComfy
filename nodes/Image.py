
class MC_SetTileSize:
    def __init__(self) -> None:
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "widthDiv": ("FLOAT", {"default": 1.0, "step": 0.001, "round": False}),
                "heightDiv": ("FLOAT", {"default": 1.0, "step": 0.001, "round": False}),
            }
        }

    RETURN_TYPES = ("INT", "INT",)
    RETURN_NAMES = ("WIDTH", "HEIGHT")

    FUNCTION = 'set_tile_size'
    CATEGORY = "ComfyMC/Image/Simple Resolution"

    def set_tile_size(self, image, widthDiv, heightDiv):
        #size = get_image_size(image)
        new_width = int(image.shape[2] / widthDiv) if widthDiv != 0 else image.shape[2]
        new_height = int(image.shape[1] / heightDiv) if heightDiv != 0 else image.shape[1]
        return new_width, new_height
