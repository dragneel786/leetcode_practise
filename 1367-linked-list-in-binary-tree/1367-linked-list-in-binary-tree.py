# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # print("Main", head.val if head else head, root.val if root else root)
        if root is None:
            return False
        
        if root.val == head.val and self.is_path(root, head):
            return True
        
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def is_path(self, root, head):
        print(head.val if head else head, root.val if root else root)
        if head is None:
            return True
        
        if root is None:
            return False
        
        return root.val == head.val and (self.is_path(root.left, head.next) or self.is_path(root.right, head.next)) 
        
        
            
        
        