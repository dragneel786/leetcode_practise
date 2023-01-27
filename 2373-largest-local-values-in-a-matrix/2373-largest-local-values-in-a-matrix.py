class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def update(m, n):
            nonlocal msize
            for r in range(max(0, m - 2), min(m + 1, msize)):
                for c in range(max(0, n - 2), min(n + 1, msize)):
                    r1, c1 = r % (size - 2), c % (size - 2)
                    max_local[r1][c1] = max(grid[m][n], max_local[r1][c1])
        
        size = len(grid)
        msize = size - 2
        max_local = [([0] * msize) for _ in range(msize)]
        for i in range(size):
            for j in range(size):
                update(i, j)
        
        return max_local