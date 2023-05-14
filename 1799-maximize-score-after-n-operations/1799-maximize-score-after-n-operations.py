class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # for a, b in combinations(nums, 2):
        #     print(a, b)
        
        @lru_cache(None)
        def score(op = 1, mask = 0):
#             if(len(used) == len(nums)):
#                 return 0
            
            ans = 0
            for i in range(len(nums)):
                if(mask & (1 << (i + 1))):
                    continue
                    
                mask = mask | (1 << (i + 1))
                for j in range(i + 1, len(nums)):
                    if(mask & (1 << (j + 1))):
                        continue
                        
                    mask = mask | (1 << (j + 1))
                    ans = max(ans, score(op + 1, mask) +\
                             op * gcd(nums[i], nums[j]))
                    mask = mask ^ (1 << (j + 1))

                mask = mask ^ (1 << (i + 1))
                
            return ans
        
        return score()