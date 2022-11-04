class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left = 0
        right = len(s) - 1
        s = list(s)
        
        while(left < right):
            if(s[left].lower() in vowels):
                while(s[right].lower() not in vowels):
                    right -= 1
                
                s[left], s[right] = s[right], s[left]
                right -= 1
                
            left += 1
        
        return "".join(s)
        