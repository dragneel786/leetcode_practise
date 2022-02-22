class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = ord(columnTitle[0]) - 64
        for i in range(1, len(columnTitle)):
            col_num = col_num * 26 + (ord(columnTitle[i]) - 64)
        return col_num