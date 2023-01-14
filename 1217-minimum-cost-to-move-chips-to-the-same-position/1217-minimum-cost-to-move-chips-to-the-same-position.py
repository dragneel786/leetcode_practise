class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        min_steps = inf
        for p1 in position:
            steps = 0
            for p2 in position:
                if(abs(p2 - p1) & 1):
                    steps += 1
            
            min_steps = min(min_steps, steps)
        
        return min_steps