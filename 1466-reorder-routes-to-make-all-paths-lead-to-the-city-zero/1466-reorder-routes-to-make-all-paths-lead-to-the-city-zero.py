class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        def make_graph():
            g = defaultdict(list)
            for a, b in connections:
                g[a].append((b, 1))
                g[b].append((a, 0))
            return g
        
        graph = make_graph()
        minc = 0
        visited = set([0])
        q = deque([(0, 0)])
        while(q):
            node, is_in = q.popleft()
            minc += is_in
            for v, d in graph[node]:
                if(v not in visited):
                    visited.add(v)
                    q.append((v, d))
        
        return minc