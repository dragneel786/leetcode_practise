# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        
        def traverse(node):
            if not node:
                return 0, True
            
            left, is_perl = traverse(node.left)
            right, is_perr = traverse(node.right)
            perfect = (left == right and is_perl and is_perr)
            if perfect:
                heappush(heap, left + right + 1)
                if len(heap) > k:
                    heappop(heap)
            
            return left + right + 1, perfect
        
        heap = []
        traverse(root)
        # print(heap)
        return heap[0] if len(heap) == k else -1