from .nodes.Logic import *
from .nodes.Conditioning import *
from .nodes.Image import *

NODE_CLASS_MAPPINGS = {
    ###  Nodes
    "MC Switch Seed": MC_SwitchSeed,
    "MC Alter Seed": MC_AlterSeed,
    "MC Set Tile Size": MC_SetTileSize,
    "MC Multi Concat": MC_MultiConditioningConcat,
}

__all__ = ['NODE_CLASS_MAPPINGS']

