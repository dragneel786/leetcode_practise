class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        if(k == len(nums)):
            return reduce(lambda a, b: a & b, nums)
        
        if(k == 1):
            return reduce(lambda a, b: a | b, nums)
        
        kor = 0
        bit_set = [0] * 32
        for num in nums:
            i = 0
            while(num):
                if(1 & num):
                    bit_set[i] += 1
                i += 1
                num >>= 1
        
        
        res = 0
        for i, b in enumerate(bit_set):
            if(b >= k):
                res += (1 << i)

        return res
                
                
                