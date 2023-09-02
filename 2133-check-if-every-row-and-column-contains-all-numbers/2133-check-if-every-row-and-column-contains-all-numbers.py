class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        elements = set([i + 1 for i in range(n)])
        
        for i in range(n):
            values = set()
            for j in range(n):
                values.add(matrix[j][i])
            
            if(len(elements - values) > 0 or\
               len(elements - set(matrix[i])) > 0):
                return False
        
        return True
    
                