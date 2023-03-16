# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def create_tree(start, end):
            if(start > end):
                return None
            
            val = postorder.pop()
            idx = imap[val]
            root = TreeNode(val)
            root.right = create_tree(idx + 1, end)
            root.left = create_tree(start, idx - 1)
            return root
        
        imap = {v: i for i, v in enumerate(inorder)}
        return create_tree(0, len(inorder) - 1)