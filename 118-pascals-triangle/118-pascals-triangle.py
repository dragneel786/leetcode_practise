class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            ans = [1]
            for j in range(1, len(res[-1])):
                ans.append(res[i - 1][j - 1] + res[i - 1][j])
            ans.append(1)
            res.append(ans)
        return res