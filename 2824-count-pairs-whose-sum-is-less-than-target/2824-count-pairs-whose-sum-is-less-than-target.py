class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        tot = 0
        n = len(nums)
        j = 0
        for i in range(n - 1, 0, -1):
            while(j < i and nums[i] + nums[j] < target):
                j += 1
            
            if(j >= i):
                break
            
            tot += j
        
        return tot + (j * (j + 1)) // 2
                