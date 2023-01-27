class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        idxs = defaultdict(lambda:-1)
        for i, c in enumerate(s):
            v = distance[ord(c) - 97]
            if(idxs[c] != -1 and \
               (i - idxs[c] - 1) != v):
                return False
            
            idxs[c] = i
        
        return True
                
                