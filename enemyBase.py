from scavengeable import Scavengeable

class EnemyBase(Scavengeable):
    def __init__(self, maxDurability, resourceDrops, possibleItemDrops : list[str], itemDropChance: int):
        self.itemDropChance = itemDropChance
        self.possibleItemDrops = possibleItemDrops
        super(maxDurability, resourceDrops)