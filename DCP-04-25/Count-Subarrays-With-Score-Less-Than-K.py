class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = start = tot = 0
        print(k)
        for end in range(len(nums)):
            tot += nums[end]
            while(start < end and tot * (end - start + 1) >= k):
                tot -= nums[start]
                start += 1
            
            # print(nums[start: end + 1], tot, (end - start + 1), k)
            if(tot * (end - start + 1) < k):
                res += (end - start + 1)
        
        return res
                
