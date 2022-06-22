class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = []
        for i,s in enumerate(servers):
            free.append((s, i, 0))

        heapify(free)
        n = len(tasks)
        busy, res = [], []
        currTime = k = 0
        while(k < n):
            while(busy and busy[0][0] <= currTime):
                _, s, i = heappop(busy)
                heappush(free, (s, i, 0))
            
            while(free and currTime >= k and k < n):
                s, i, _ = heappop(free)
                heappush(busy, (currTime + tasks[k], s, i))
                res.append(i)
                k += 1
            
            if(not free):
                currTime = busy[0][0]
            else:
                currTime = k

        return res