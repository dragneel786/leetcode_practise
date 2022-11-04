class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        left = 0
        right = len(s) - 1
        s = list(s)
        
        while(left < right):
            check1 = s[left].lower() not in vowels
            check2 = s[right].lower() not in vowels
            
            if(not check1 and not check2):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                
            left += check1
            right -= check2
            
        
        return "".join(s)
        