class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        new_mat = []
        for c in range(cols):
            mat = []
            for r in range(rows):
                mat.append(matrix[r][c])
            
            new_mat.append(mat)
        
        return new_mat