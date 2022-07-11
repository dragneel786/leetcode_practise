# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        def getLeftMostCol(r):
            if(not binaryMatrix.get(r, cols - 1)): return -1
            lo, hi = 0, cols - 1
            found = False
            while(lo <= hi):
                mid = ((hi - lo) >> 1) + lo
                v = binaryMatrix.get(r, mid)
                if(v == 1):
                    found = True
                    hi = mid - 1
                else:
                    lo = mid + 1
            return lo if(found) else -1
        
        rows, cols = binaryMatrix.dimensions()
        leftmost = inf
        for r in range(rows):
            idx = getLeftMostCol(r)
            if(idx != -1):
                leftmost = min(leftmost, idx)
        return leftmost if(leftmost != inf) else -1
                    
            
            