class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        st = deque()
        drc = [(2, 1), (1, 2), (-1, 2), (-2, 1), \
               (-2, -1), (-1, -2), (1, -2), (2, -1)]
        st.append((0, 0, 0))
        visit = set([(0, 0)])
        while(st):
            for _ in range(len(st)):
                r, c, m = st.popleft()
                if((r, c) == (x, y)):
                    return m
                for dr, dc in drc:
                    nr, nc = r + dr, c + dc
                    if((nr, nc) not in visit):
                        visit.add((nr, nc))
                        st.append((nr, nc, m + 1))