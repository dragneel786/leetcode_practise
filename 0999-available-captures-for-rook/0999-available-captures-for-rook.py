class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        def dfs(r, c):
            count = 0
            for dr, dc in [(0, 1), (1, 0),\
                           (-1, 0), (0, -1)]:

                nr, nc = r + dr, c + dc
                while(0 <= nr < rows and 0 <= nc < cols):
                    
                    if(board[nr][nc] != '.'):
                        count += (board[nr][nc] == 'p')
                        break
                    
                    nr, nc = nr + dr, nc + dc

            return count
    
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if(board[r][c] == 'R'):
                    return dfs(r, c)
        
        return 0
                    
            
            