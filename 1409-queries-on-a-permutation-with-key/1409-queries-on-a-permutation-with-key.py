class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res = []
        perm = [i for i in range(m, 0, -1)]
        for q in queries:
            idx = perm.index(q)
            res.append(m - idx - 1)
            perm.pop(idx)
            perm.append(q)
        
        return res