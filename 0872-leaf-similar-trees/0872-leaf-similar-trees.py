# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def inorder(root, op):
            if(not root):
                return
            
            if(not root.left and not root.right):
                if(not op and q and q[0] == root.val):
                    q.popleft()
                else:
                    q.append(root.val)

            inorder(root.left, op)
            inorder(root.right, op)
            
        q = deque()
        inorder(root1, True)
        inorder(root2, False)
        return len(q) == 0