class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        def crush():
            nonlocal rows, cols
            cells = set()
            find(rows, cols, cells)
            is_crushed = len(cells) > 0
            for a, b in cells:
                board[a][b] = 0
            
            return is_crushed

        def find(rows, cols, cells):
            row_map = {i:[-1, []] for i in range(rows)}
            col_map = {i:[-1, []] for i in range(cols)}
            for r in range(rows):
                for c in range(cols):
                    update(cells, row_map, board[r][c], r)
                    row_map[r][1].append((r, c))
                
                    update(cells, col_map, board[r][c], c)
                    col_map[c][1].append((r, c))
                
                update(cells, row_map, -1, r)
            
            for c in range(cols):
                update(cells, col_map, -1, c)
                
            return False
        
        
        def update(cells, cmap, val, s):
            if(not val or cmap[s][0] != val):
                if(len(cmap[s][1]) > 2):
                    cells.update(cmap[s][1])
                
                cmap[s] = [val, []]
            
    
        def shift():
            nonlocal rows, cols
            for c in range(cols):
                vr = rows - 1
                for r in range(rows - 1, -1, -1):
                    if(board[r][c] != 0):
                        board[vr][c], board[r][c] = board[r][c], board[vr][c]
                        while(vr >= r and board[vr][c] != 0):
                            vr -= 1

        
        rows, cols = len(board), len(board[0])
        while(crush()):
            shift()
        
        return board