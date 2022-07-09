class Solution:
    def toHex(self, num: int) -> str:
        if(num == 0): return "0"
        result = ""
        m = "0123456789abcdef"
        for i in range(8):
            result = m[(num & 15)] + result
            num = num >> 4
        return result.lstrip("0")