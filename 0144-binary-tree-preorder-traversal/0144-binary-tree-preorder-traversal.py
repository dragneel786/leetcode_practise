# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = deque([(root, 0)])
        ans = []
        while(root and st):
            node, state = st.pop()
            if(state == 0):
                ans.append(node.val)
                st.append((node, 1))
            
            if(state == 0 and node.left):
                st.append((node.left, 0))
            
            if(state == 1 and node.right):
                st.append((node.right, 0))
            
        return ans
            
        