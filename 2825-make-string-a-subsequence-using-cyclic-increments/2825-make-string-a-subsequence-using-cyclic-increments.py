class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        index2 = 0
        for c in str1:
            if index2 >= len(str2):
                break
                
            inc_ch = chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
            if c == str2[index2] or inc_ch == str2[index2]:
                index2 += 1
                
        return index2 >= len(str2)