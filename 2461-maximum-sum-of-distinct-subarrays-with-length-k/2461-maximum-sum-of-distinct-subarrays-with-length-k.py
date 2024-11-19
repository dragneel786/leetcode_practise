class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sub_set = Counter()
        start = tot = res = 0
        for end in range(len(nums)):
            sub_set[nums[end]] += 1
            tot += nums[end]
            
            if end >= k:
                sub_set[nums[start]] -= 1
                tot -= nums[start]
                if sub_set[nums[start]] == 0:
                    del sub_set[nums[start]]
                
                start += 1
            
            
            if end >= k - 1 and len(sub_set) == k:
                res = max(res, tot)
            
            
        
        return res