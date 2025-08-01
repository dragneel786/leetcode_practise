class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = [[1]]
        for _ in range(numRows - 1):
            curr = [1]
            for i in range(len(pascals[-1]) - 1):
                curr.append(pascals[-1][i] + pascals[-1][i + 1])
            curr.append(1)
            pascals.append(curr)
        return pascals
