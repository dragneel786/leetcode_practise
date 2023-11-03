class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = n = len(nums)
        if(n == 1):
            return 1
        
        for size in range(2, n):
            uset = Counter(nums[:size])
            res += (len(uset) ** 2)
            for i in range(size, n):
                uset[nums[i - size]] -= 1
                
                if(not uset[nums[i - size]]):
                    del uset[nums[i - size]]
                
                uset[nums[i]] += 1
                res += (len(uset) ** 2)

        return res + (len(Counter(nums)) ** 2)
                
                