class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        
        def get_y_coors(n):
            top_left_x = top_left_y = top_right_x = 0
            top_right_y = n - 1
            coor = set()
            while(top_left_y != top_right_y):
                coor.add((top_left_x, top_left_y))
                coor.add((top_right_x, top_right_y))
                top_left_x += 1
                top_left_y += 1
                
                top_right_x += 1
                top_right_y -= 1
            
            while(top_right_x < n):
                coor.add((top_right_x, top_right_y))
                top_right_x += 1
            
            return coor
                
        
        n = len(grid)
        y_coors = get_y_coors(n)
        y0 = y1 = y2 = 0
        ny0 = ny1 = ny2 = 0
        for r in range(n):
            for c in range(n):
                val = grid[r][c]
                zero, one, two = val == 0, val == 1, val == 2
                if((r, c) in y_coors):
                    y0 += zero
                    y1 += one
                    y2 += two
                
                else:
                    ny0 += zero
                    ny1 += one
                    ny2 += two
                    
        
        y_len = len(y_coors)
        ny_len = n - y_len
        return min(y1 + y2 + ny0 + min(ny1, ny2),\\
                   y0 + y2 + ny1 + min(ny0, ny2),\\
                   y0 + y1 + ny2 + min(ny0, ny1))
    
                    
                