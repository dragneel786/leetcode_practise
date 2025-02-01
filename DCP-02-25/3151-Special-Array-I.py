from itertools import islice
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        ans = idx = 0
        for i in range(0, len(tasks), 4):
            max_val = max(tasks[i:i + 4])
            ans = max(ans, processorTime[idx] + max_val)
            idx += 1
        
        return ans
                
            
            
            
            
        
        
        