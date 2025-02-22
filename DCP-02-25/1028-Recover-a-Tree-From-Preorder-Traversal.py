# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def parse_traversal():
            st = deque()
            curr = num = 0
            for c in traversal + "-":
                if c.isdigit():
                    num = (num * 10) + int(c)
                else:
                    if num > 0:
                        st.append((curr, num))
                        curr = num = 0

                    curr += 1

            return st

        def construct_tree(level):
            nonlocal stack
            if not stack or stack[0][0] < level:
                return

            _, val = stack.popleft()
            node = TreeNode(val)
            node.left = construct_tree(level + 1)
            node.right = construct_tree(level + 1)
            return node

        stack = parse_traversal()
        root = construct_tree(0)
        print(stack, root.val)
        return root
 