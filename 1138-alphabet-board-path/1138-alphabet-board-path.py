class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ox, oy = 0, 0
        res = ""
        for c in target:
            val = ord(c) - 97
            nx, ny = val // 5, val % 5
            res += (max(0, oy - ny) * 'L')
            res += (max(0, nx - ox) * 'D')
            res += (max(0, ox - nx) * 'U')
            res += (max(0, ny - oy) * 'R') + "!"
            ox, oy = nx, ny
        return res
                