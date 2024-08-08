class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ret = []
        curr = [[-1]]
        edges = 1
        while(len(curr)):
            curr = []
            # Right
            for _ in range(edges):
                if -1 < rStart < rows and -1 < cStart < cols:
                    curr.append([rStart, cStart])
                
                cStart += 1
            
            # Down
            for _ in range(edges):
                if -1 < rStart < rows and -1 <cStart < cols:
                    curr.append([rStart, cStart])
                
                rStart += 1
            
            edges += 1
            
            # Left
            for _ in range(edges):
                if -1 < rStart < rows and -1 <cStart < cols:
                    curr.append([rStart, cStart])
                
                cStart -= 1
            
            # Up
            for _ in range(edges):
                if -1 < rStart < rows and -1 <cStart < cols:
                    curr.append([rStart, cStart])
                
                rStart -= 1
            
            edges += 1
            ret.extend(curr)
        
        return ret
                
            
            
            
            
        