class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def create_heap():
            g = []
            for i, (x1, y1) in enumerate(points):
                for j, (x2, y2) in enumerate(points[i + 1:]):
                    dis = abs(x1 - x2) + abs(y1 - y2)
                    heappush(g, (dis, i, j + i + 1))

            return g
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return False
            
            parent[pb] = pa
            return True
        
        def find(a):
            if(parent[a] != a):
                parent[a] = find(parent[a])
            return parent[a]
    
        heap = create_heap()
        parent = {i:i for i in range(len(points))}
        n = len(points) - 1
        ans = 0
        while(n and heap):
            dis, x, y = heappop(heap)
            if(union(x, y)):
                ans += dis
                n -= 1
        
        return ans
            
                
            
    
        
                
                
        
        
        
        
        
            
                    
                
                