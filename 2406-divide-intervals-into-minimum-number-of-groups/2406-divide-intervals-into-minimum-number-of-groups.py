class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        max_val = 0
        for s, e in intervals:
            max_val = max(max_val, e)
        
        values = [0] * (max_val + 2)
        for s, e in intervals:
            values[s] += 1
            values[e + 1] -= 1
        
        max_rep = 0
        for i in range(1, max_val + 2):
            values[i] += values[i - 1]
            max_rep = max(max_rep, values[i])
        
        return max_rep
            