class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = list()
        n = len(nums)
        for i in range(n - 2):
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            j = i + 1
            k = n - 1
            while(j < k):
                if(j > i + 1 and nums[j] == nums[j - 1]):
                    j += 1
                    continue
                if(k < n - 1 and nums[k] == nums[k + 1]):
                    k -= 1
                    continue
                val = nums[i] + nums[j] + nums[k]
                if(val == 0):
                    ans.append([nums[i], nums[j], nums[k]])
                if(val < 0):
                    j += 1
                else:
                    k -= 1
        return ans