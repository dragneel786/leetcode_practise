class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        def construct_graph():
            nonlocal rows, cols
            g = defaultdict(dict)
            for r in range(rows):
                for c in range(cols):

                    curr_idx = c + r * cols
                    for i, (dr, dc) in enumerate([(0,1),(0,-1),(1,0),(-1,0)]):
                        nr, nc = r + dr, c + dc
                        
                        if 0 <= nr < rows and 0 <= nc < cols:
                            new_idx = nc + nr * cols
                            g[curr_idx][new_idx] = not (grid[r][c] == (i + 1))
            
            return g
        
        rows, cols = len(grid), len(grid[0])
        size = (rows * cols)
        graph = construct_graph()
        visited = [inf] * size
        visited[0] = 0
        heap = [(0, 0)]
        while(heap):
            cost, node = heappop(heap)
            if node == (size - 1):
                return cost

            for ve, va in graph[node].items():
                if cost + va < visited[ve]:
                    visited[ve] = cost + va
                    heappush(heap, (cost + va, ve))

        return inf
        
        


