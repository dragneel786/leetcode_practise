# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        def subTrees(root):
            if(not root):
                return ""
            
            left = subTrees(root.left)
            right = subTrees(root.right)
            res = ("L" + left) + ("R" + right) + "(" + str(root.val) + ")"
            if(sub[res] == 0):
                ans.add(root)
                sub[res] = 1
            elif(sub[res] == -1):
                sub[res] = 0
            return res
            
        
        ans = set()
        sub = defaultdict(lambda:-1)
        subTrees(root.left)
        subTrees(root.right)
        return ans