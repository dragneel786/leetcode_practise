class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count = 0
        hashed = set()
        res = []
        for a, b in zip(A, B):
            if(a in hashed):
                count += 1
            
            if(b in hashed):
                count += 1
            
            if(a == b):
                count += 1
            
            # print(a, b, hashed)
            res.append(count)
            hashed.add(a)
            hashed.add(b)
        
        return res
            