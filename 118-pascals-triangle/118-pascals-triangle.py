class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]
        for n in range(2, numRows):
            temp = [1]
            for i in range(n - 1):
                temp.append(sum(res[-1][i:i + 2]))
            temp.append(1)
            res.append(temp)
        return res[:numRows]