"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        newNode = Node()
        if(self.checkSame(grid)):
            newNode.isLeaf = True
            newNode.val = grid[0][0]
            return newNode
        
        n = len(grid)
        ns = n // 2
        sgrid = [([0] * ns) for _ in range(ns)]
        #top Right.
        for r in range(ns):
            for c in range(ns):
                sgrid[r][c] = grid[r][c]
        newNode.topLeft = self.construct(sgrid)
        
        #top left
        for r in range(ns):
            for c in range(ns, n):
                sgrid[r][c - ns] = grid[r][c]
        newNode.topRight = self.construct(sgrid)
        
        #top Right.
        for r in range(ns, n):
            for c in range(ns):
                sgrid[r - ns][c] = grid[r][c]
        newNode.bottomLeft = self.construct(sgrid)
        
        #top Right.
        for r in range(ns, n):
            for c in range(ns, n):
                sgrid[r - ns][c - ns] = grid[r][c]
        newNode.bottomRight = self.construct(sgrid)
        
        return newNode
        
    def checkSame(self, grid):
        ones, zeros = 0, 0
        s = len(grid)
        for r in range(s):
            for c in range(s):
                if(grid[r][c]):
                    ones += 1
                else:
                    zeros += 1
                if(ones and zeros):
                    return False
        return True