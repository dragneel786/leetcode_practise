# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = [root]
        for node in self.tree:
            if(node.left): self.tree.append(node.left)
            if(node.right): self.tree.append(node.right)
        
    def insert(self, val: int) -> int:
        n = len(self.tree)
        self.tree.append(TreeNode(val))
        idx = (n - 1) // 2
        if(n % 2): self.tree[idx].left = self.tree[-1]
        else: self.tree[idx].right = self.tree[-1]
        return self.tree[idx].val
        
        
    def get_root(self) -> Optional[TreeNode]:
        return self.tree[0]

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()