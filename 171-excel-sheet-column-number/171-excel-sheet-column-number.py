class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        powI = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            col_num += (ord(columnTitle[i]) - 64) * (26 ** powI)
            powI += 1
        
        return col_num