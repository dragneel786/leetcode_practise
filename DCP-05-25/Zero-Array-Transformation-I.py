class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        pos = [0] * (n + 1)
        for i, j in queries:
            pos[i] -= 1
            pos[j + 1] += 1
        
        curr = 0
        for i in range(n):
            curr += pos[i]
            nums[i] += curr
            if nums[i] > 0:
                return False
        
        return True
             