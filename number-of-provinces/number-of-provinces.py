class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        cols = len(isConnected)
        count = 0
        for row in range(rows):
            for col in range(cols):
                if(isConnected[row][col] == 1):
                    isConnected[row][col] = 0
                    self.inDirect(isConnected, row)
                    count += 1
        return count

    def inDirect(self, mat, row):
        for i in range(len(mat[0])):
            if(mat[row][i] == 1):
                mat[row][i] = 0
                self.inDirect(mat, i)