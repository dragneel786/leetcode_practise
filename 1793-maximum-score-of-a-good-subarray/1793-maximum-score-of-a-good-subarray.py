class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i = j = k
        n = len(nums)
        min_val = nums[k]
        res = min_val
        while(i > 0 or j < n - 1):
            if(i == 0 or (j < n - 1 and nums[i - 1] < nums[j + 1])):
                j += 1
            else:
                i -= 1
            
            min_val = min(min_val, nums[i], nums[j])
            res = max(res, min_val * (j - i + 1))
            
        return res