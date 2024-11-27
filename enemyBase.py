'''
@author: Lucian Kath
@version: 1.0

@datum: 2024-11-26

@description: Basisklasse der im Spiel enthaltenen Gegner
'''

from scavengeable import Scavengeable

class EnemyBase(Scavengeable):
    def __init__(self, maxDurability, resourceDrops, possibleItemDrops : list[str], itemDropChance: int):
        self.itemDropChance = itemDropChance
        self.possibleItemDrops = possibleItemDrops
        super(maxDurability, resourceDrops)