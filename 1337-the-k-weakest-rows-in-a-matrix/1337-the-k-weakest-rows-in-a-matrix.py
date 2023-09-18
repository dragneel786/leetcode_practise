class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [ele[1] for ele in nsmallest(k, [(m.count(1), i) for i,m in enumerate(mat)])]
        