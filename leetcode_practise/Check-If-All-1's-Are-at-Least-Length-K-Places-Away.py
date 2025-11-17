class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        j = -1000000
        for i in range(len(nums)):
            if nums[i] == 1:
                # print(i, j)
                if (i - j - 1) < k:
                    return False
                
                j = i
        
        return True