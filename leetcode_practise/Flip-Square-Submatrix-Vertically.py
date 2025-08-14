class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k):
            for c in range(y, y + k):
                nr = x + i
                dr = x + k - i - 1
                if nr > dr:
                    break
                
                grid[nr][c], grid[dr][c] = \
                grid[dr][c], grid[nr][c]

                # print((nr, c), (dr, c))
        
        return grid
                        




