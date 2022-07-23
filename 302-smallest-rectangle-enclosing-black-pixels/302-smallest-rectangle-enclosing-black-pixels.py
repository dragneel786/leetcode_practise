class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        def dfs(x, y):
            nonlocal mmx, mmy
            if(x < 0 or x >= m or y < 0 or y >= n or image[x][y] != "1"):
                return
            
            image[x][y] = "-1"
            x1, x2 = mmx
            mmx = [min(x1, x), max(x2, x)]
            
            y1, y2 = mmy
            mmy = [min(y1, y), max(y2, y)]
            
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(x + dx, y + dy)
        
        mmx = [x, x]
        mmy = [y, y]
        m, n = len(image), len(image[0])
        dfs(x, y)
        return (abs(mmx[0] - mmx[1]) + 1) * (abs(mmy[0] - mmy[1]) + 1)