class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        char_map = [0] * 26
        count = 0
        
        for c in s:
            char_map[ord(c) - 97] += 1
            
            if(char_map[ord(c) - 97] & 1):
                count += 1
            else:
                count -= 1
        
        return count <= 1
            
        
        
    