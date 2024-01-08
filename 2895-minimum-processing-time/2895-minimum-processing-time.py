from itertools import islice
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks = iter(sorted(tasks, reverse=True))
        ans = 0
        for p in processorTime:
            max_val = 0
            for v in islice(tasks, 4):
                max_val = max(max_val, v)
            
            ans = max(ans, p + max_val)
        
        return ans
                
            
            
            
            
        
        
        