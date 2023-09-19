# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def construct(start = 0, end = len(nums)):
            if(start >= end):
                return None
            
            max_val = max(nums[start: end])
            idx = indexes[max_val]
            new_node = TreeNode(max_val)
            new_node.left = construct(start, idx)
            new_node.right = construct(idx + 1, end)
            return new_node
        
        indexes = {num:i for i, num in enumerate(nums)}
        return construct()
        