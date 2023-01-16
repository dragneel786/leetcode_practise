class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort()
        n = len(nums)
        ans = [0] * n
        prev = [-1, -1]
        for i in range(n):
            val, idx = nums[i]
            if(prev[0] == val):
                ans[idx] = ans[prev[1]]
            else:
                ans[idx] = i
            
            prev = nums[i]
        
        return ans