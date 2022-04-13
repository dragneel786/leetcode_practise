class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        val = 1
        mat = [([0] * n) for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        d = 0
        while(top <= bottom and left <= right):
            if(d == 0):
                for i in range(left, right + 1):
                    mat[top][i] = val
                    val += 1
                top += 1

            elif(d == 1):
                for i in range(top, bottom + 1):
                    mat[i][right] = val
                    val += 1
                right -= 1

            elif(d == 2):
                for i in range(right, left - 1, -1):
                    mat[bottom][i] = val
                    val += 1
                bottom -= 1

            else:
                for i in range(bottom, top - 1, -1):
                    mat[i][left] = val
                    val += 1
                left += 1

            d = (d + 1) % 4

        return mat