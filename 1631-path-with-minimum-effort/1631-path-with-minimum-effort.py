class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        st = []
        rows, cols = len(heights), len(heights[0])
        dist = [([math.inf] * cols) for _ in range(rows)]
        st.append([0, [0, 0]])
        while(len(st)):
            node = heappop(st)
            weight = node[0]
            r = node[1][0]
            c = node[1][1]
            if(r == rows - 1 and c == cols - 1):
                return weight
            if(dist[r][c] < weight):
                continue
            for d in [[0,1], [0,-1], [1,0],[-1,0]]:
                dr = r + d[0]
                dc = c + d[1]
                if(dr < 0 or dr >= rows or dc < 0 or dc >= cols):
                    continue  
                newWeight = max(weight, abs(heights[dr][dc] - heights[r][c]))
                if(dist[dr][dc] <= newWeight):
                    continue
                dist[dr][dc] = newWeight
                heappush(st, [newWeight, [dr, dc]])
        return 0
                
                
            
            
            
            
            