class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        @lru_cache(None)
        def max_time(i, s = 1):
            if(i >= len(satisfaction)):
                return 0
            
            return max(s * satisfaction[i] +\
                        max_time(i + 1, s + 1),\
                        max_time(i + 1, s))
            
        
        satisfaction.sort()
        return max_time(0)