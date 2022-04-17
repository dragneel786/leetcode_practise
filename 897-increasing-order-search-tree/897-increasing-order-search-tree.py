# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def makeNode(root, head, join = [None]):
            if(not root):
                return None
            
            makeNode(root.left, head, join)
            
            if(not head[0]):
                head[0] = root
            else:
                join[0].right = root
            join[0] = root
            
            root.left = None
            makeNode(root.right, head, join)
            
            while(root.right):
                root = root.right
                
            return root
        
        head = [None]
        makeNode(root, head)
        return head[0]