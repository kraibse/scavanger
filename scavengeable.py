class Scavengeable:
    def __init__(self, maxDurability : int, resourceDrops : int):
        self.resourceDrops = resourceDrops
        self.maxDurability = maxDurability
        self.durability = maxDurability

    def scavenge(self, damage) -> int:
        self.durability = max(0, self.durability - damage)
        if self.durability <= 0 and self.isFullyScavenged:
            self.onFullyScavenged()
        return self.resourceDrops * (damage / self.maxDurability)
    
    def onFullyScavenged(self):
        self.isFullyScavenged = True
        pass