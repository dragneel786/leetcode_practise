class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = inf
        for i, num in enumerate(nums):
            if(num == target):
                if(abs(i - start) < ans):
                    ans = abs(i - start)
                else:
                    return ans
        
        return ans
        