class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @lru_cache(None)
        def score(op = 1, mask = 0):  
            ans = 0
            for i in range(len(nums)):
                if((mask >> i) & 1):
                    continue
                    
                mask = mask | (1 << i)
                for j in range(i + 1, len(nums)):
                    if((mask >> j) & 1):
                        continue
                        
                    mask = mask | (1 << j)
                    ans = max(ans, score(op + 1, mask) +\
                             op * gcd(nums[i], nums[j]))
                    mask = mask ^ (1 << j)

                mask = mask ^ (1 << i)
                
            return ans
        
        return score()