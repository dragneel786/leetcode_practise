class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        
        run_sum = max_val = neededTime[0]
        count, ans = 1, 0
        n = len(colors)
        
        for i in range(1, n):
            if(colors[i] != colors[i - 1]):
                if(count > 1):
                    ans += (run_sum - max_val)
                
                count = 0
                run_sum = max_val = 0
            
            count += 1
            run_sum += neededTime[i]
            max_val = max(neededTime[i], max_val)
        
        if(count > 1):
            ans += (run_sum - max_val)
        
        return ans
                    
        
            