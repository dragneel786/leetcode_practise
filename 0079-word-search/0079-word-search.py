class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r, c, i):
            if(i == len(word)):
                return True
            
            for dr, dc in [(0, 1), (1, 0),\
                           (0, -1), (-1, 0)]:
                
                nr, nc = r + dr, c + dc
                if(0 <= nr < rows and 0 <= nc < cols
                   and word[i] == board[nr][nc]):
                    
                    board[nr][nc], ch = '-', board[nr][nc]
                    if(dfs(nr, nc, i + 1)):
                        return True
                    board[nr][nc] = ch
                
            return False
    
    
    
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if(board[r][c] == word[0]):
                    board[r][c], ac = '-', board[r][c]
                    if(dfs(r, c, 1)):
                        return True
                    board[r][c] = ac
        
        return False
                    