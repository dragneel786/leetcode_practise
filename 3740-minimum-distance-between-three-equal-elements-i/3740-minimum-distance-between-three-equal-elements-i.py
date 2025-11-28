class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indexes = defaultdict(list)
        for i, num in enumerate(nums):
            indexes[num].append(i)
        
        res = inf
        for values in indexes.values():
            if len(values) > 2:
                for i in range(len(values) - 2):
                    d1 = abs(values[i] - values[i + 1])
                    d2 = abs(values[i + 1] - values[i + 2])
                    d3 = abs(values[i + 2] - values[i])
                    res = min(res, d1 + d2 + d3)
            
        return res if res != inf else -1

        
