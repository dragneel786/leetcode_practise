class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        j = 0
        maxSub = 0
        sub = 0
        nums = nums + [nums[-1]]
        seen = defaultdict(lambda:0)
        for i in range(len(nums)):
            if(seen[nums[i]]):
                maxSub = max(sub, maxSub)
                
            while(j < i and seen[nums[i]]):
                sub -= nums[j]
                seen[nums[j]] -= 1
                j += 1
            
            sub += nums[i]
            seen[nums[i]] += 1
        
        return maxSub
            