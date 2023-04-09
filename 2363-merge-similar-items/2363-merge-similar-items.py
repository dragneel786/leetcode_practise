class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        vmap1 = Counter({v:w for v, w in items2})
        vmap2 = Counter({v:w for v, w in items1})
        return sorted([[v, w] for v, w in (vmap1 + vmap2).items()])
            