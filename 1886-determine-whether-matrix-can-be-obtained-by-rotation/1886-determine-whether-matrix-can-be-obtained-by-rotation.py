class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def make90(mat):
            res = []
            for i in range(len(mat)):
                temp = []
                for j in range(len(mat) - 1, -1, -1):
                    temp.append(mat[j][i])
                res.append(temp)
            return res
            
        for _ in range(4):
            if(mat == target):
                return True
            mat = make90(mat)
        
        return False
                