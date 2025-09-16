class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse=True)
        res = []
        for i in range(len(nums)):
            if len(res) >= k:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            res.append(nums[i])
        
        return res