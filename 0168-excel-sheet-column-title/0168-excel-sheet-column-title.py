class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        li = []
        while(columnNumber >= 26):
            rem = columnNumber % 26
            li.append(chr(64 + (rem if(rem != 0) else 26)))
            columnNumber -= rem == 0
            columnNumber //= 26
        
        if(columnNumber):
            li.append(chr(64 + columnNumber))
        return ''.join(li[::-1])
            