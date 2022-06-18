class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_idx = []
        for i, t in enumerate(tasks):
            task_idx.append((t[1], i, t[0]))
        task_idx.sort(key=lambda x:x[2])
        
        n = len(tasks)
        res = []
        i = 1
        pq = [task_idx[0]]
        t = pq[-1][2]
        while(len(res) < n):
            while(i < n and (not pq or task_idx[i][2] <= t)):
                if(t < task_idx[i][2]):
                    t = task_idx[i][2]
                heappush(pq, task_idx[i])
                i += 1
                
            task = heappop(pq)
            res.append(task[1])
            t += task[0]
        
        return res
            
            
        