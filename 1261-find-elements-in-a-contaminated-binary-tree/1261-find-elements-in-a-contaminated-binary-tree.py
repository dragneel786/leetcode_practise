# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        
        def cleanse(node, val = 0):
            if(not node):
                return
        
            temp_val = val * 2 + 1
            cleanse(node.left, temp_val)
            cleanse(node.right, temp_val + 1)
            self.maps.add(val)
                
        self.maps = set()
        cleanse(root)

    def find(self, target: int) -> bool:
        return target in self.maps


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)