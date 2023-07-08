class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if(k == 1):
            return 0
        
        vals = []
        for i in range(1, len(weights)):
            vals.append(weights[i - 1] + weights[i])
        
        vals.sort()
        k -= 1
        return sum(vals[-k:]) - sum(vals[:k])