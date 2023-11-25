class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = sum([abs(nums[0] - a) for a in nums[1:]])
        ans = [right]
        for i, a in enumerate(nums[1:], 1):
            diff = a - nums[i - 1]
            left += (diff * i)
            right -= (diff * (n - i))
            ans.append(left + right)
        
        return ans
            