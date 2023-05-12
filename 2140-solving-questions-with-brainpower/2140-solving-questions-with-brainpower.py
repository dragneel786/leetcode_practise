class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @lru_cache(None)
        def solve(i):
            if(i >= len(questions)):
                return 0
            
            po, inc = questions[i]
            return max(solve(i + inc + 1) + po, solve(i + 1))
        
        return solve(0)