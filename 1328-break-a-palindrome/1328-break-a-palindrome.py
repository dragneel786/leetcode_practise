class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if(n == 1): return ''
        
        palin = list(palindrome)
        for i, c in enumerate(palin):
            if(c != 'a' and i != floor(n / 2)):
                palin[i] = 'a'
                return ''.join(palin)
        
        palin[-1] = 'b'
        return ''.join(palin)