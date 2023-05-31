class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -(k + 1)
        for i, num in enumerate(nums):
            if(not num):
                continue
            
            if(i - prev - 1 < k):
                return False
            
            prev = i
        
        return True
                