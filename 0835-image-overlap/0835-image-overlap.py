class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        
        def prefix_mat(A, B, startAI, startAJ):
            rcount = lcount = 0
            startBI = startBJ = 0
            for i in range(startAI, n):
                startBJ = 0
                for j in range(startAJ, n):
                    if(A[i][j] == 1 and \
                       A[i][j] == B[startBI][startBJ]):
                        lcount += 1
                        
                    if(A[i][startBJ] == 1 and \
                       A[i][startBJ] == B[startBI][j]):
                        rcount += 1
                    startBJ += 1
                startBI += 1
            
            return max(lcount, rcount)
                
            
        n = len(A)
        ans = 0
        for r in range(n):
            for c in range(n):
                print(r, c)
                ans = max(ans, prefix_mat(A, B, r, c),\
                          prefix_mat(B, A, r, c), )
        
        return ans