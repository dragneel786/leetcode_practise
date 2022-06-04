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
            p = st.pop()
            c = 0
            levels = l.split(",")
            for i in range(len(levels)):
                node = None
                if(levels[i] != "N"):
                    node = TreeNode(int(levels[i]))
                    st.appendleft(node)
                if(c == 0):
                    p.left = node
                elif(c == 1):
                    p.right = node
                    if(i + 1 < len(levels)):
                        p = st.pop()
                c = (c + 1) % 2
        
        return root.left
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans