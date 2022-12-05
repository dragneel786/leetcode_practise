class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        count = [0] * 1001
        for num in nums:
            count[num] += 1
        
        lo = 1
        hi = 1000
        res = -1
        while(lo <= hi):
            if(lo + hi >= k or not count[hi]):
                hi -= 1
            else:
                if(count[lo] > (0 if(lo < hi) else 1)):
                    res = max(lo + hi, res)
                
                lo += 1
                
        return res
                
        