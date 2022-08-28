class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sort_and_update(x, y):
            temp = []
            for a in range(max(m, n)):
                if(x + a < m and y + a < n):
                    temp.append(mat[x + a][y + a])
            
            temp.sort()
            for a in range(max(m, n)):
                if(x + a < m and y + a < n):
                    mat[x + a][y + a] = temp[a]
            
            
        
        m, n = len(mat), len(mat[0])
        for i in range(m):
            sort_and_update(i, 0)
        
        for j in range(1, n):
            sort_and_update(0, j)
        
        return mat
        
            
        