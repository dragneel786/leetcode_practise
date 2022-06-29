class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        #greedy
        res = 0
        x, y = abs(x), abs(y)
        while(x > 4 or y > 4):
            res += 1
            if(x >= y):
                x -= 2
                y -= 1 if(y >= 1) else -1
            else:
                x -= 1 if(x >= 1) else -1
                y -= 2
        
        st = deque()
        drc = [(2, 1), (1, 2), (-1, 2), (-2, 1), \
               (-2, -1), (-1, -2), (1, -2), (2, -1)]
        st.append((0, 0, 0))
        visit = set([(0, 0)])
        while(st):
            for _ in range(len(st)):
                r, c, m = st.popleft()
                if((r, c) == (x, y)):
                    return m + res
                for dr, dc in drc:
                    nr, nc = r + dr, c + dc
                    if((nr, nc) not in visit):
                        visit.add((nr, nc))
                        st.append((nr, nc, m + 1))