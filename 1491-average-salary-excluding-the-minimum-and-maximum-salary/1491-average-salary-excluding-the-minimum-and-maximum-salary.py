class Solution:
    def average(self, salary: List[int]) -> float:
        tot = 0
        min_val = inf
        max_val = -inf
        for s in salary:
            min_val = min(min_val, s)
            max_val = max(max_val, s)
            tot += s
        
        return (tot - (min_val + max_val)) / (len(salary) - 2)