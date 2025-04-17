class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counts = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    counts += 1
        
        return counts
