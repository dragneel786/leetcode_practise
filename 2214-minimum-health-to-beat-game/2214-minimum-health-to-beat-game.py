class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        damage.sort()
        idx = bisect_right(damage, armor)
        if(idx == len(damage)):
            damage[-1] -= min(armor, damage[-1])
        else:
            damage[idx] -= min(armor, damage[idx])
        
        return sum(damage) + 1
        