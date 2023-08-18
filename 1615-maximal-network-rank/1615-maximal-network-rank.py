class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        def create_network():
            g = defaultdict(set)
            for i, (a, b) in enumerate(roads):
                g[a].add(i)
                g[b].add(i)
            
            return g
        
        
        graph = create_network()
        res = 0
        for a in range(n):
            an = len(graph[a])
            for b in range(a + 1, n):
                bn = len(graph[b])
                res = max(res, an + bn - len(graph[a] & graph[b]))
        
        return res
        