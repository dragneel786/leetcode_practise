class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        min_steps = inf
        poss = Counter(position)
        for key in poss.keys():
            steps = 0
            for k, v in poss.items():
                if(abs(key - k) & 1):
                    steps += (1 * v)
                    
            min_steps = min(min_steps, steps)
        
        return min_steps