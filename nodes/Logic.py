from typing import Callable, Mapping

DEFAULT_INT = ("INT", {"default": 0})

class MC_SwitchSeed:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed1": (
                    "INT",
                    {
                        "default": 0,
                        "min": -1e9,
                        "max": 1e9,
                        "forceInput": True,
                    },
                ),
                "seed2": (
                    "INT",
                    {
                        "default": 0,
                        "min": -1e9,
                        "max": 1e9,
                        "forceInput": True,
                    },
                ),
                "Input": ("INT", {"default": 1, "min": 1, "max": 2}),
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("seed",)
    CATEGORY = "ComfyMC/Utils/Logic"
    FUNCTION = "execute"

    def execute(self, Input, seed1, seed2,):
        #logger.debug("seed switch: " + str(boolean))
        if Input == 1:
            return (seed1,)
        else:
            return (seed2,)

class MC_AlterSeed:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "op": (list(INT_BINARY_OPERATIONS.keys()),),
                "seed": ("INT",{"forceInput": True,},),
                "modify": DEFAULT_INT,
            }
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("seed",)
    FUNCTION = "op"
    CATEGORY = "ComfyMC/Utils/Logic"

    def op(self, op: str, seed: int, modify: int) -> tuple[int]:
        return (INT_BINARY_OPERATIONS[op](seed, modify),)
    
INT_BINARY_OPERATIONS: Mapping[str, Callable[[int, int], int]] = {
    "Add": lambda a, b: a + b,
    "Sub": lambda a, b: a - b,
    "Mul": lambda a, b: a * b,
    "Div": lambda a, b: a // b,
}
