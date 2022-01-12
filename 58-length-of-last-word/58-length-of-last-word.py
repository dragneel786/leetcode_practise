class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        leng_last = 0
        found = False
        for i in range(len(s) - 1, -1, -1):
            if(s[i] == " " and found):
                return leng_last


            if(s[i] != " "):
                found = True
                leng_last += 1

        return leng_last
