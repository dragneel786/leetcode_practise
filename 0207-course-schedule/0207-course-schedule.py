class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def create_graph():
            for a, b in prerequisites:
                preq[a].append(b)
                in_degree[b] += 1
            
        preq = defaultdict(list)
        in_degree = [0] * numCourses
        create_graph()
        
        q = deque([a for a in range(numCourses) if(not in_degree[a])])
        counts = 0
        while(q):
            node = q.popleft()
            for v in preq[node]:
                in_degree[v] -= 1
                if(not in_degree[v]):
                    q.append(v)
        
            counts += 1
        
        return counts == numCourses