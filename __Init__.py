from .nodes.Logic import *
from .nodes.Conditioning import *
from .nodes.Image import *

NODE_CLASS_MAPPINGS = {
    ###  Nodes
    "MC Switch Seed": MC_SwitchSeed,
    "MC Switch Image": MC_SwitchImage,
    "MC Switch Latent": MC_SwitchLatent,
    "MC Switch Model": MC_SwitchModel,
    "MC Switch String": MC_SwitchString,
    "MC Alter Seed": MC_AlterSeed,
    "MC Set Tile Size": MC_SetTileSize,
    "MC Get Image Size": MC_GetImageSize,
    "MC Multi Concat": MC_MultiConditioningConcat,
    "MC Multi Concat(Advanced)": MC_MultiConditioningConcatAdvanced,
}

__all__ = ['NODE_CLASS_MAPPINGS']

