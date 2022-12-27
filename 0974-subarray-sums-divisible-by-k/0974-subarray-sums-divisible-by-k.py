class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        pd = defaultdict(int)
        pd[0] = 1
        count = tot = 0
        
        for num in nums:
            tot += num
            mod = tot % k
            
            count += pd[mod]
            pd[tot % k] += 1
    
        return count
            