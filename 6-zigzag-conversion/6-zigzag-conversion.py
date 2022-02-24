class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        mat = ["" for _ in range(numRows)]
        idx = 1
        dir = 1
        for i in s:
            mat[idx - 1] += i
            idx += dir
            if(idx == 0 or idx > numRows):
                dir *= -1
                idx += (2 * dir)

        return "".join(mat)
    