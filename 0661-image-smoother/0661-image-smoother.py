class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        new_img = [([0] * n) for _ in range(m)]
        for r in range(m):
            for c in range(n):
                div = 1
                new_img[r][c] = img[r][c]
                for dr, dc in [(1,0),(0,1),(0,-1),(-1,0),\
                               (-1,1),(1,-1),(1,1),(-1,-1)]:
                    nr, nc = r + dr, c + dc
                    if(0 <= nr < m and 0 <= nc < n):
                        new_img[r][c] += img[nr][nc]
                        div += 1
                
                new_img[r][c] //= div
        
        return new_img
        
            
                        
                        
                    