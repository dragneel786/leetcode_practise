class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = sum(cell << (i * n + j) for i, row in enumerate(mat)\
                 for j, cell in enumerate(row))
        q = deque([(start, 0)])
        seen = {start}
        while(q):
            for _ in range(len(q)):
                curr, step = q.popleft()
                if(not curr):
                    return step
                for i in range(m):
                    for j in range(n):
                        nex = curr
                        nex = nex ^ (1 << (i * n + j))
                        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            ni, nj = i + di, j + dj
                            if(m > ni >= 0 <= nj < n):
                                nex ^= (1 << (ni * n + nj))
                        if(nex not in seen):
                            seen.add(nex)
                            q.append((nex, step + 1))
        return -1
                            
