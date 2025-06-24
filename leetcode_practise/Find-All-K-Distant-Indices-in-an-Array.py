class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keys_idx = []
        for i, val in enumerate(nums):
            if val == key:
                keys_idx.append(i)
        
        res = []
        for i, val in enumerate(nums):
            for idx in keys_idx:
                if abs(idx - i) <= k:
                    res.append(i)
                    break
        
        return res