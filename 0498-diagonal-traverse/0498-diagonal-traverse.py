class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r = c = 0
        rows, cols = len(mat), len(mat[0])
        res = list()
        while(r < rows):
            curr = list()
            nr, nc = r, c
            while(-1 < nr < rows and -1 < nc < cols):
                curr.append(mat[nr][nc])
                nr -= 1
                nc += 1
            
            res.append(curr)
            r += 1
        
        r -= 1
        c += 1
        while(c < cols):
            curr = list()
            nr, nc = r, c
            while(-1 < nr < rows and -1 < nc < cols):
                curr.append(mat[nr][nc])
                nr -= 1
                nc += 1
            
            res.append(curr)
            c += 1
         
        ret = []
        for i, r in enumerate(res):
            if i % 2 == 1:
                r.reverse()
            ret.extend(r)
        return ret
        
            
            