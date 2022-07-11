# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def getRightView(root, l):
            if(not root):
                return
            
            if(len(rightView) == l):
                rightView.append(root.val)

            getRightView(root.right, l + 1)
            getRightView(root.left, l + 1)
        
        rightView = []
        getRightView(root, 0)
        return rightView        
        