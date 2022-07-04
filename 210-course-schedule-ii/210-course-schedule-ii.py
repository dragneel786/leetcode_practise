class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda:[])
        ind = [0] * numCourses
        for p in prerequisites:
            graph[p[1]].append(p[0])
            ind[p[0]] += 1
        
        q = deque()
        taken = 0
        res = []
        for i,d in enumerate(ind):
            if(not d):
                q.append(i)
                
        while(q):
            for _ in range(len(q)):
                c = q.popleft()
                taken += 1
                res.append(c)
                for v in graph[c]:
                    ind[v] -= 1
                    if(ind[v] == 0):
                        q.append(v)
        
        return res if(taken == numCourses) else []
                
                    
            