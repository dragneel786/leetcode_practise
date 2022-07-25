# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def genTrees(values):
            if(not values):
                return [None]
            
            ret = []
            for i, v in enumerate(values):
                left = genTrees(values[:i])
                right = genTrees(values[i + 1:])
                for l in left:
                    for r in right:
                        newNode = TreeNode(v)
                        newNode.left = l
                        newNode.right = r
                        ret.append(newNode)
            return ret
            
        values = [i for i in range(1, n + 1)]
        return genTrees(values)
            
            