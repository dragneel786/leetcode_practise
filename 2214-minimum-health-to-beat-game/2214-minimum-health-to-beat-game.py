class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        maxv = 0
        sums = 0
        for d in damage:
            maxv = max(d, maxv)
            sums += d
        
        return (sums - min(maxv, armor) + 1)
        