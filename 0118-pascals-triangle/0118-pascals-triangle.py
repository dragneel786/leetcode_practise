class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1], [1,1]]
        for _ in range(numRows - 2):
            node = [1]
            for i in range(len(ans[-1]) - 1):
                node.append(ans[-1][i] + ans[-1][i + 1])
            node.append(1)
            ans.append(node)
    
        return ans[:numRows]
                