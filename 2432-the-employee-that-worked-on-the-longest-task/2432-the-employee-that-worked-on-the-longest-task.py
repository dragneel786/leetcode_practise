class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prev_time = 0
        ans = [0, 0]
        for a, t in logs:
            diff = t - prev_time 
            prev_time = t
            
            if(diff > ans[1] or \
               (diff == ans[1] and a < ans[0])):
                ans = [a, diff]
        
        return ans[0]