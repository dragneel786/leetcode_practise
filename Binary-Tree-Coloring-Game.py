class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix) + 1, len(matrix[0]) + 1
        ps = [([0] * cols) for _ in range(rows)]
        for row in range(1, rows):
            for col in range(1, cols):
                ps[row][col] = ps[row - 1][col] + ps[row][col - 1] - \\
                ps[row - 1][col - 1] + matrix[row - 1][col - 1]
        
        
        count = 0
        for r1 in range(1, rows):
            for r2 in range(r1, rows):
                has = defaultdict(int)
                has[0] = 1
                
                for c in range(1, cols):
                    curr = ps[r2][c] - ps[r1 - 1][c]
                    count += has[curr - target]
                    has[curr] += 1
        
        return count