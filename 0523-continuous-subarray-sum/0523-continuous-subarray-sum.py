class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        def check_and_append(imap, psum, index):
            j = psum // k
            while(j > -1):
                diff = psum - (k * j)
                if(diff in imap and imap[diff] < index - 1):
                    return True
                j -= 1
            return False
        
        
        psum = nums[0]
        imap = {0:-1}
        imap[psum] = imap.get(psum, 0)
        for i, num in enumerate(nums[1:], 1):
            psum += num
            
            if(check_and_append(imap, psum, i)):
                return True
            
            imap[psum] = imap.get(psum, i)
        
        return False
            
            