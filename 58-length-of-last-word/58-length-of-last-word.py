class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        leng_last = 0
        for i in s[::-1]:
            if(i == " "):
                if(leng_last):
                    break
            else:
                leng_last += 1

        return leng_last
