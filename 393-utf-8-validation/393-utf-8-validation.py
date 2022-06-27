class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        binR = []
        for d in data:
            b = bin(d)[2:]
            binR.append((8 - len(b)) * '0' + bin(d)[2:])
        
        h = {"0":0, "110":1, "1110":2, "11110":3}
        form = 0
        for b in binR:
            if(form == 0):
                if(b[0] in h):
                    form = 0
                elif(b[:5] in h):
                    form = h[b[:5]]
                elif(b[:4] in h):
                    form = h[b[:4]]
                elif(b[:3] in h):
                    form = h[b[:3]]
                else:
                    return False
            else:
                if(b[:2] != "10"):
                    return False
                form -= 1
        return form == 0
            
            
            