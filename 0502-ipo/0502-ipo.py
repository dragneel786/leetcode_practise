class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [[c, p] for p, c in zip(profits, capital)]
        projects.sort()
        i = 0
        heap = []
        while k > 0:
            while i < len(projects) and projects[i][0] <= w:
                heappush(heap, -projects[i][1])
                i += 1
            
            if not heap:
                break
                
            w -= heappop(heap)
            k -= 1
        
        return w
            
            
        
        
            
        
        