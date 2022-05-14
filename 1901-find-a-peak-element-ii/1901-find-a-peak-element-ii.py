class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        l = 0
        h = m - 1
        while(l <= h):
            mid = (h - l) // 2 + l
            maxVI = [-math.inf, 0]
            for i in range(len(mat[mid])):
                if(mat[mid][i] > maxVI[0]):
                    maxVI = [mat[mid][i], i]
                
            if((mid == 0 or maxVI[0] > mat[mid - 1][maxVI[1]]) and \
              (mid == m - 1 or maxVI[0] > mat[mid + 1][maxVI[1]])):
                return [mid, maxVI[1]]
            
            if((mid == 0 or maxVI[0] > mat[mid - 1][maxVI[1]])):
                l = mid + 1
            else:
                h = mid - 1
        
                