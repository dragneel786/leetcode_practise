# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        st = deque([root])
        res = []
        while(st):
            temp = []
            for _ in range(len(st)):
                node = st.popleft()
                temp.append(node.val)
                if(node.left):
                    st.append(node.left)
                if(node.right):
                    st.append(node.right)
            res.append(temp)
        return res