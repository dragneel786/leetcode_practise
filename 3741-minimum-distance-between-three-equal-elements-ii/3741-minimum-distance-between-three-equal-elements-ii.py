class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = dict()
        for i, num in enumerate(nums):
            indices.setdefault(num, [])
            indices[num].append(i)
        
        min_val = inf
        for indexes in indices.values():
            if len(indexes) < 3:
                continue
            
            for i in range(len(indexes) - 2):
                a, b, c = indexes[i: i + 3]
                abs_sum = abs(a - b) + abs(b - c) + abs(c - a)
                min_val = min(abs_sum, min_val)
        
        if min_val == inf:
            return -1
        
        return min_val
            