class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if(n == 1):
            return True
        
        if(not nums[0]):
            return False
        
        res = [False] * n
        res[n - 1] = True
        for i in range(n - 2,  -1, -1):
            for j in range(1, nums[i] + 1):
                if(i + j < n):
                    if(res[i + j]):
                        res[i] = res[i + j]
                        break

        return res[0]