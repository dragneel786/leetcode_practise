class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = False
        for i in range(len(num) - 1, -1, -1):
            if(int(num[i]) & 1):
                odd = True
                break
        
        return num[:i + 1] if(odd) else ""
        
        