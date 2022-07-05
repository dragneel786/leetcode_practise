class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        shrink = 0
        for expand in range(len(nums)):
            k -= 1 - nums[expand]
            if(k < 0):
                k += 1 - nums[shrink]
                shrink += 1
        
        return expand - shrink + 1