class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        def union(x, y):
            px, py = find(x), find(y)
            if(px != py):
                parent[py] = px

        def find(x):
            if(parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]


        def islands(r, c):
            nonlocal i
            idx = (c * m) + r
            ans[i] = ans[i - 1]
            if(parent[idx] != -1):
                return 

            items = set()
            parent[idx] = idx
            for dr, dc in [(0, 1), (1, 0),\
                            (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if(0 <= nr < m and 0 <= nc < n):
                    val = (nc * m) + nr
                    pval = find(val)
                    if(pval != -1):
                        items.add(pval)
                        union(val, idx)

            ans[i] += 1 - len(items)


        parent = {i:-1 for i in range(m * n)}
        parent[-1] = -1

        size = len(positions)
        ans = [0] * size
        for i, (sr, sc) in enumerate(positions):
            islands(sr, sc)

        return ans
            
        
        
                