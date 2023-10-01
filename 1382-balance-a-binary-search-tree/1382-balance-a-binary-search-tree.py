# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def preorder(node):
            if(not node):
                return 
            
            preorder(node.left)
            ordered.append(node.val)
            preorder(node.right)
        
        def construct(start, end):
            if(start > end):
                return None
            
            mid = (start + end) // 2
            print(ordered[mid])
            node = TreeNode(ordered[mid])
            node.left = construct(start, mid - 1)
            node.right = construct(mid + 1, end)
            return node
        
        ordered = []
        preorder(root)
        return construct(0, len(ordered) - 1)
        