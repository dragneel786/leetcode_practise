class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        tcounter = Counter(text)
        bcounts = [('b', 1), ('a', 1),\
                   ('l',2), ('o', 2), ('n', 1)]
        counts = 0
        while(True):
            for k, c in bcounts:
                if(tcounter.get(k, 0) < c):
                    return counts
                
                tcounter[k] -= c
            
            counts += 1
                    
                                      