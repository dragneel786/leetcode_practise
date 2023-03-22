class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        for a, b, d in roads:
            graph[a].add((b, d))
            graph[b].add((a, d))
        
        q = deque([(1, inf)])
        ans = inf
        while(q):
            node, dis = q.popleft()  
            for v, d in graph[node]:
                q.append((v, dis))
                ans = min(d, ans)
            
            del graph[node]
            
        return ans