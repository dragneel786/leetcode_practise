class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        def min_effort(sr, sc, visited = set()):
            if(sr >= rows - 1 and sc >= cols - 1):
                return 0
            
            min_path = inf
            for dr, dc in [(0,1),(0,-1),(-1,0),(1,0)]:
                nr, nc = sr + dr, sc + dc
                if(0 <= nr < rows and 0 <= nc < cols\
                   and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    path = max(min_effort(nr, nc, visited),
                               abs(heights[sr][sc] - heights[nr][nc]))
                    min_path = min(min_path, path)
                    visited.discard((nr, nc))
            
            return min_path
                    
        rows, cols = len(heights), len(heights[0])
        heap = [(0,0,0)]
        visited = defaultdict(lambda:inf)
        visited[(0,0)] = 0
        while(heap):
            effort, sr, sc = heappop(heap)
            if(sr >= rows - 1 and sc >= cols - 1):
                return effort
            
            for dr, dc in [(0,1),(0,-1),(-1,0),(1,0)]:
                nr, nc = sr + dr, sc + dc
                if(0 <= nr < rows and 0 <= nc < cols):
                    diff = abs(heights[sr][sc] - heights[nr][nc])
                    curr_effort = max(effort, diff)
                    
                    if(visited[(nr,nc)] > curr_effort):
                        visited[(nr, nc)] = curr_effort
                        heappush(heap, (curr_effort, nr, nc))
        
                    
        