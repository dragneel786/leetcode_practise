# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        rows, cols = binaryMatrix.dimensions()
        c = cols - 1
        for r in range(rows - 1, -1, -1):
            while(c > -1 and binaryMatrix.get(r, c)):
                c -= 1
            if(c < 0):
                return 0    
        return (c + 1) if(c + 1 < cols) else -1
                    
            
            