class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        
        def sub_sum(size):
            curr_sum = start = 0
            res = inf
            for end in range(len(nums)):
                curr_sum += nums[end]
                if end >= size:
                    curr_sum -= nums[start]
                    start += 1
                
                if end >= size - 1 and curr_sum > 0:
                    res = min(res, curr_sum)
                
                # print(curr_sum)
            
            return res
        
        
        val = inf
        for s in range(l, r + 1):
            val = min(val, sub_sum(s))
        
        return val if val != inf else -1
                