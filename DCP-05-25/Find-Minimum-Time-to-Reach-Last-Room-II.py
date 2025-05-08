class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        heap = [(0, 0, 0, 0)]
        visited = dict()
        moveTime[0][0] = -1
        while(heap):
            dis, x, y, state = heappop(heap)
            if (x, y) == (m - 1, n - 1):
                return dis
            
            for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if moveTime[nx][ny] == -1:
                        continue

                    val = max(dis, moveTime[nx][ny]) + (state + 1)
                    heappush(heap, (val, nx, ny, (state + 1) % 2))
                    moveTime[nx][ny] = -1
        
        return -1



        