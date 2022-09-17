class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        op = {i : (s, t) for i, s, t in zip(indices, sources, targets)}

        i = j = 0
        res = ''

        while(i < len(s)):
            if(i in op and s[i : i + len(op[i][0])] == op[i][0]):
                src, tar = op[i]
                res += tar
                i = i + len(src)
                continue

            res += s[i]
            i += 1

        return res
                
            
            