class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # return 4
        def create_network():
            g = defaultdict(set)
            for i, (a, b) in enumerate(roads):
                g[a].add(i)
                g[b].add(i)
            
            return g
        
        
        graph = create_network()
        res = 0
        for a in range(n):
            for b in range(n):
                res = max(res, len(graph[a] | graph[b]))
        
        return res
        