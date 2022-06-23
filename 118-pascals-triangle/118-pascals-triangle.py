class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = [[1], [1, 1]]
        for i in range(numRows - 2):
            temp = [1]
            for j in range(1, len(pascals[-1])):
                temp.append(pascals[-1][j - 1] + pascals[-1][j])
            temp.append(1)
            pascals.append(temp)
        
        return pascals[:numRows]