from typing import Callable, Mapping

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
                "Input": ("INT", {"default": 1, "min": 1, "max": 3}),
            },
            "optional":{
                "seed3": (
                    "INT",
                    {
                        "default": 0,
                        "min": -1e9,
                        "max": 1e9,
                        "forceInput": True,
                    },
                ),
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("seed",)
    CATEGORY = "ComfyMC/Utils/Logic"
    FUNCTION = "execute"

    def execute(self, Input, seed1, seed2, seed3,):
        if Input == 1:
            return (seed1,)
        elif Input == 2:
            return (seed2,)
        else:
            return (seed3,)

class MC_AlterSeed:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "op": (list(INT_BINARY_OPERATIONS.keys()),),
                "seed": ("INT",{"forceInput": True,},),
                "modify": ("INT", {"default": 1,"min": 1}),
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

# wildcard trick is taken from pythongossss's
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any_typ = AnyType("*")

# based on impactifnone and crystools switches
class MC_SwitchString:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "on_true": ("STRING", {"forceInput": True}),
                "on_false": ("STRING", {"forceInput": True}),
                "signal": (any_typ,),
            }
        }

    CATEGORY = "ComfyMC/Utils/Logic"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)

    FUNCTION = "execute"

    def execute(self, on_true=None, on_false=None, signal=None):
        if signal == None:
            return(on_false,)
        elif signal == False:
            return(on_false,)
        elif signal == True:
            return(on_true,)
        else:
            return(on_true,)
        
class MC_SwitchImage:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "on_true": ("IMAGE", ),
                "on_false": ("IMAGE", ),
                #"signal": (any_typ,),
            }
        }

    CATEGORY = "ComfyMC/Utils/Logic"
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)

    FUNCTION = "execute"

    def execute(self, on_true=None, on_false=None):
        if on_true is not None:
            return(on_true,)
        else:
            return(on_false,)
    
class MC_SwitchLatent:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "on_true": ("LATENT", ),
                "on_false": ("LATENT", ),
                #"signal": (any_typ,),
            }
        }

    CATEGORY = "ComfyMC/Utils/Logic"
    RETURN_TYPES = ("LATENT",)
    RETURN_NAMES = ("latent",)

    FUNCTION = "execute"

    def execute(self, on_true=None, on_false=None):
        if on_true is not None:
            return(on_true,)
        else:
            return(on_false,)

class MC_SwitchModel:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "on_true": ("MODEL", ),
                "on_false": ("MODEL", ),
                #"signal": (any_typ,),
            }
        }

    CATEGORY = "ComfyMC/Utils/Logic"
    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)

    FUNCTION = "execute"

    def execute(self, on_true=None, on_false=None):
        if on_true is not None:
            return(on_true,)
        else:
            return(on_false,)