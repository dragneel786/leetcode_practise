class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cmap = {" ": " "}
        key = key.replace(" ", '')
        i = 0
        for c in key:
            if(c in cmap):
                continue
            
            cmap[c] = chr(i + 97)
            i += 1
        
        ans = []
        for c in message:
            ans.append(cmap[c])
        
        return ''.join(ans)
            
        