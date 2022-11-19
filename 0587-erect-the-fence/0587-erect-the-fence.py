class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        
        def find_slope(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            
            return ((y2 - y1) * (x3 - x2)) - ((y3 - y2) * (x2 - x1))
        
        lower = deque()
        upper = deque()
        trees.sort()
        
        for x, y in trees:
            l = len(lower)
            while(l > 1 and find_slope(lower[l - 2], lower[l - 1], (x, y)) < 0):
                l -= 1
                lower.pop()
            
            u = len(upper)
            while(u > 1 and find_slope(upper[u - 2], upper[u - 1], (x, y)) > 0):
                u -= 1
                upper.pop()
            
            lower.append((x, y))
            upper.append((x, y))
        
        return set([*lower, *upper])
                
                
            
        