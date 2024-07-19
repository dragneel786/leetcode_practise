class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_mins = []
        for row in matrix:
            idx, val = -1, inf
            for i, r in enumerate(row):
                if val > r:
                    idx = i
                    val = r
            
            row_mins.append([idx, val])
        
        for r in range(len(matrix)):
            for i, (idx, val) in enumerate(row_mins):
                if val < matrix[r][idx]:
                    row_mins[i] = [idx, inf]
                
        
        return list(set([val for _, val in row_mins if val != inf]))
                
                
                
            
        
        
        
        
            
                