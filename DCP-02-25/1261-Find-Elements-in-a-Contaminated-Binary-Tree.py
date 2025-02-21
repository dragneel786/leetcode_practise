# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nums = set()
        self.traverse(root, 0)

    def find(self, target: int) -> bool:
        return target in self.nums
        
    def traverse(self, node, val):
        if not node:
            return
        
        self.nums.add(val)
        self.traverse(node.left, 2 * val + 1)
        self.traverse(node.right, 2 * val + 2)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)