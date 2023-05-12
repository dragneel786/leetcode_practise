class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        
        def solve(i):
            if(i >= len(questions)):
                return 0
            
            if(i not in memo):
                po, inc = questions[i]
                memo[i] = max(solve(i + inc + 1) + po,\
                              solve(i + 1))
            
            return memo[i]
        
        memo = dict()
        return solve(0)