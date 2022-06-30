class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def getPermute(li, op = ""):
            if(not li):
                res.append(op + mid + op[::-1])
                return
            
            for i in range(len(li)):
                if(i > 0 and li[i] == li[i - 1]):
                    continue
                getPermute(li[:i] + li[i + 1:], op + li[i])
        
        counts = Counter(s)
        mid, odd = "", 0
        li = []
        for c in counts.keys():
            if(counts[c] & 1):
                odd += 1
                mid = c
            for _ in range(counts[c] // 2):
                li.append(c)       
        if(odd > 1): return []    
        
        li.sort()
        res = []
        getPermute(li)
        return res
        
        
        