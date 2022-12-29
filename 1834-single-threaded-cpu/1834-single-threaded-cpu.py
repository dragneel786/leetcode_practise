class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_idx = [[a, b, i] for i, (a, b) in enumerate(tasks)]
        task_idx.sort()
        
        curr_time = ti = 0
        heap = [(1, -1)]
        ans = []
        n = len(tasks)
        while(heap):
            ptime, idx = heappop(heap)
            ans.append(idx)
            curr_time += ptime
        
            while((ti < n and curr_time >= task_idx[ti][0])\
                  or (not heap and ti < n)):
                ptime, pro, index = task_idx[ti]
                curr_time = max(ptime, curr_time)
                heappush(heap, (pro, index))
                ti += 1
                
        return ans[1:]
            
            
            
                
            