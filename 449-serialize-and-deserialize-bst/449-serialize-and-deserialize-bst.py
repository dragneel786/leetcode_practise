# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        st = deque()
        ans = ""
        st.append(root)
        while(len(st)):
            for _ in range(len(st)):
                node = st.pop()
                if(not node):
                    ans += "N,"
                    continue
                ans += str(node.val) + ","
                st.appendleft(node.left)
                st.appendleft(node.right)
            ans = ans[:-1] + "|"
        return ans[:-1]

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        root = TreeNode()
        st = deque()
        st.append(root)
        for l in data.split("|"):
            levels = l.split(",")
            for i in range(0, len(levels), 2):
                node = st.pop()
                left, right = None, None
                if(levels[i] != "N"):
                    left = TreeNode(int(levels[i]))
                    st.appendleft(left)
                    
                if(i + 1 < len(levels) and levels[i + 1] != "N"):
                    right = TreeNode(int(levels[i + 1]))
                    st.appendleft(right)
                
                node.left = left
                node.right = right
        return root.left
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans