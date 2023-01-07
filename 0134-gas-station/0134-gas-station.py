class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total_tank = curr_tank = 0
        ans = 0
        for i, (co, ga) in enumerate(zip(cost, gas)):
            val = ga - co
            total_tank += val
            curr_tank += val
        
            if(curr_tank < 0):
                curr_tank = 0
                ans = i + 1
            
            
        
        return ans if(total_tank >= 0) else -1

        
        