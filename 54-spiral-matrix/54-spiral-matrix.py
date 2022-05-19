class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        up = left = 0
        right = cols - 1
        down = rows - 1
        result = []

        while (len(result) < rows * cols):
            for i in range(left, right + 1):
                result.append(matrix[up][i])

            for j in range(up + 1, down + 1):
                result.append(matrix[j][right])

            if(up != down):
                for i in range(right - 1, left - 1, -1):
                    result.append(matrix[down][i])

            if(right != left):
                for j in range(down - 1, up, -1):
                    result.append(matrix[j][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result