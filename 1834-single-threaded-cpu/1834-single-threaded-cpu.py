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
        
            while(ti < n and curr_time >= task_idx[ti][0]):
                _, pro, index = task_idx[ti]
                heappush(heap, (pro, index))
                ti += 1
            
            if(not heap and ti < n):
                curr_time, pro, index = task_idx[ti]
                heappush(heap, (pro, index))
                ti += 1

        return ans[1:]
            
            
            
                
            