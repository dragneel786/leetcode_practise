class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        values = [(a, i) for i, a in enumerate(arr)]
        values.sort()
        res = [0] * len(arr)
        prev = -inf
        rank = 0
        for v, i in values:
            if prev != v:
                prev = v
                rank += 1
            
            res[i] = rank
        
        return res
                