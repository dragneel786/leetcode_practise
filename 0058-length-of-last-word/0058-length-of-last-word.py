class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for word in s.split(" "):
            if(len(word) != 0):
                ans = len(word)
        
        return ans