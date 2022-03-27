class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        n = min(math.ceil(rows / 2), math.ceil(cols / 2))
        for k in range(n):
            i, j = k, k
            inc = 1
            for _ in range(min(rows - k - i, cols - k - j, 2)):
                while(j < cols - k and j > -1 + k):
                    res.append(matrix[i][j])
                    j += inc

                j -= inc
                i += inc
                while(i < rows - k and i > -1 + k):
                    if((k, k) == (i, j)):
                        break
                    res.append(matrix[i][j])
                    i += inc
                i -= inc
                j -= inc

                inc = -1
        return res