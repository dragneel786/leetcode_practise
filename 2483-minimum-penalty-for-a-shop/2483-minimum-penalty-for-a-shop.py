class Solution:
    def bestClosingTime(self, customers: str) -> int:
        early = 0
        curr_penalty = min_penalty = customers.count('Y')
        for i, c in enumerate(customers + '-'):
            if(c == 'Y'):
                curr_penalty -= 1
            else:
                curr_penalty += 1
            
            if(min_penalty > curr_penalty):
                early = i + 1
                min_penalty = curr_penalty
            
        return early
            
            
        