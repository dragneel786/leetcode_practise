class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        imap = {0: 0}
        psum = 0
        for i, num in enumerate(nums):
            psum += num
            mod = psum % k
            
            if(imap.get(mod, inf) < i):
                return True
            
            if(mod not in imap):
                imap[mod] = i + 1
        
        return False
            
            