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
        
        def helper(x, y, n):
            if(n == 1):
                return Node(grid[x][y], True)
            
            result = Node()
            topLeft = helper(x, y, n // 2)
            topRight = helper(x, y + n // 2, n // 2)
            bottomLeft = helper(x + n // 2, y, n // 2)
            bottomRight = helper(x + n // 2, y + n // 2, n // 2)
            if(topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and\
               topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                result.isLeaf = True
                result.val = grid[x][y]
            else:
                result.topLeft = topLeft
                result.topRight = topRight
                result.bottomLeft = bottomLeft
                result.bottomRight = bottomRight
            return result
            
        return helper(0, 0, len(grid))
                