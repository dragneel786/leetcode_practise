class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        parent = {i:i for i in range(n)}
        def union(x, y):
            nonlocal parent
            px, py = find(x), find(y)
            if px != py:
                parent[py] = find(px)


        def find(x):
            nonlocal parent
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                union(i, i - 1)

        res = []
        for a, b in queries:
            if find(a) == find(b):
                res.append(True)
            else:
                res.append(False)

        return res
