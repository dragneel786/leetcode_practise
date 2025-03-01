class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        counts = 0
        common = Counter()
        
        for a, b in zip(A, B):
            common[a] += 1
            if common[a] == 2:
                counts += 1
            
            common[b] += 1
            if common[b] == 2:
                counts += 1
            
            res.append(counts)
        
        return res
