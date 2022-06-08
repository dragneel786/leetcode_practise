class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        rep = []
        for i in range(len(indices)):
            rep.append((indices[i], sources[i], targets[i]))
        rep.sort(key=lambda x: x[0])
        
        res = ""
        i = 0
        for r in rep:
            while(i != r[0]):
                res += s[i]
                i += 1
                
            if(s[i: i + len(r[1])] == r[1]):
                res += r[2]
                i += len(r[1])
        
        while(i != len(s)):
            res += s[i]
            i += 1
        
        return res
            
        