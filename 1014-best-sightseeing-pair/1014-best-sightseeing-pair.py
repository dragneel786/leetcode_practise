class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        curr = values[-1] - 1
        res = float('-inf')
        for i in range(len(values) - 2, -1, -1):
            res = max(res, curr + values[i])
            curr = max(curr, values[i])
            curr -= 1
        
        return res