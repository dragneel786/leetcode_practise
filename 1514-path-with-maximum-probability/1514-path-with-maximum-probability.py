class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        def create_graph():
            g = defaultdict(list)
            for w, (a, b) in zip(succProb, edges):
                g[a].append((b, w))
                g[b].append((a, w))
                
            return g
        
        graph = create_graph()
        heap = [(-1, start_node)]
        visited = [-inf] * n
        visited[start_node] = 1
        while(heap):
            value, curr_node = heappop(heap)
            value = -value
            if curr_node == end_node:
                return value
            for node, wei in graph[curr_node]:
                if visited[node] < (wei * value):
                    visited[node] = (wei * value)
                    heappush(heap, (-(wei * value), node))
            
        
        return 0
            
            
            
            
        
        
        
        