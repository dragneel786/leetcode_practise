class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        size = (2 * k) + 1
        if(n < size):
            return res
        
        tot = 0
        for i, num in enumerate(nums):
            tot += num
            if(i >= size - 1):
                if(i > size - 1):
                    tot -= nums[i - size]
                
                
                res[i - k] = tot // size
        
        return res
                
            