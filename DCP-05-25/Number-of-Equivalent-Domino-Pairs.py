class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = Counter()
        res = 0
        for a, b in dominoes:
            v1 = counts[(a,b)]
            v2 = counts[(b,a)]
            
            if a == b:
                v2 = 0
            
            res += (v1 + v2)
            counts[(a,b)] += 1

        return res
            