class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pmap = defaultdict(int)
        pair = 0
        for a, b in dominoes:
            v1 = pmap[(a, b)]
            v2 = pmap[(b, a)]
            
            if(a == b):
                v2 = 0
            
            pair += (v1 + v2)
            pmap[(a, b)] += 1
        
        return pair
            