# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if(n % 2 == 0):
            return []
        
        def genTrees(n):
            if(n == 1):
                return [TreeNode(0)]

            res = []
            for m in range(1, n, 2):
                left = genTrees(m)
                right = genTrees(n - m - 1)
                for l in left:
                    for r in right:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
        
        return genTrees(n)