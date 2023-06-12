class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        nums.append(inf)
        start = nums[0]
        for i in range(1, len(nums)):
            if(nums[i - 1] + 1 == nums[i]):
                continue
            
            if(nums[i - 1] == start):
                ans.append(str(start))
            else:
                ans.append(f'{start}->{nums[i - 1]}')
            
            start = nums[i]
        
        return ans
            
            