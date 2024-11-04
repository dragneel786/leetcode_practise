class Solution:
    def compressedString(self, word: str) -> str:
        curr = 1
        ch = word[0]
        res = []
        for c in word[1:] + '-':
            if ch != c or curr == 9:
                res.append(f'{curr}{ch}')
                ch = c
                curr = 0
            
            curr += 1
        
        return ''.join(res)
            