class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sub_sum = sum(nums) - x
        n = len(nums)
        size = inf
        tot = j = 0
        for i in range(n):
            tot += nums[i]
            while(j <= i and tot > sub_sum):
                tot -= nums[j]
                j += 1
            
            if(tot == sub_sum):
                size = min(n - (i - j + 1), size)
        
        return size if(size != inf) else -1
            