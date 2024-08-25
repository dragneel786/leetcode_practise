# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = deque([(root, 0)])
        res = []
        while(len(st)):
            node, t_type = st.pop()
            if not node:
                continue
                
            if t_type == 0:
                st.append((node, 1))
                st.append((node.left, 0))
            
            elif t_type == 1:
                st.append((node, 2))
                st.append((node.right, 0))
            
            else:
                res.append(node.val)
        
        return res
        