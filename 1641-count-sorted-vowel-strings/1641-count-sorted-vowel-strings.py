class Solution:
    def countVowelStrings(self, n: int) -> int:
        chs = ['a', 'e', 'i', 'o', 'u']
        count = [0]
        
        def genCombo(chs, op = ""):
            if(len(op) == n):
                count[0] += 1
                return
            
            if(not chs):
                return
            
            genCombo(chs, op + chs[0])
            genCombo(chs[1:], op)
            
        genCombo(chs)
        return count[0]