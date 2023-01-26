class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        def create_graph():
            g = defaultdict(list)
            for a, b, cost in flights:
                g[a].append((b, cost))
            return g
            
        
        graph = create_graph()
        visited = defaultdict(lambda:inf)
        visited[src] = 0
        q = deque([(src, 0)])
        stops = 0
        ans = inf
        while(q and stops <= k + 1):
            for _ in range(len(q)):
                node, costs = q.popleft()
                if(node == dst):
                    ans = min(costs, ans)
                    
                for ne, co in graph[node]:
                    if(visited[ne] > co + costs):
                        q.append((ne, co + costs))
                        visited[ne] = co + costs
            
            stops += 1
        
        return ans if(ans != inf) else -1
                        
                
        