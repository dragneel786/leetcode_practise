class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        def create_graph():
            nonlocal n
            g = defaultdict(list)
            degree = [0] * n
            for a, b in roads:
                g[a].append(b)
                g[b].append(a)
                degree[a] += 1
                degree[b] += 1
            
            return g, degree
        
        
        def bfs(seats):
            q = deque()
            for i in range(1, n):
                if(degree[i] == 1):
                    q.append(i)
                    degree[i] -= 1
                    
            reps = [1] * n
            cost = 0
            while(q):
                e = q.popleft()
                cost += ceil(reps[e] / seats)
                for v in graph[e]:
                    degree[v] -= 1
                    reps[v] += reps[e]
                    if(degree[v] == 1 and v != 0):
                        q.append(v)
                        degree[v] -= 1
                    
            return cost
                        
        n = len(roads) + 1
        graph, degree = create_graph()
        return bfs(seats)