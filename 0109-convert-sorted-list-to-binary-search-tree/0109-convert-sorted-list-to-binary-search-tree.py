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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def create_tree(vals):
            n = len(vals)
            if(n <= 1):
                return TreeNode(vals[0]) if(n) else None
            
            mid = n // 2
            node = TreeNode(vals[mid])
            node.left = create_tree(vals[0:mid])
            node.right = create_tree(vals[mid + 1:])
            return node
            
        values = []
        while(head):
            values.append(head.val)
            head = head.next
        
        return create_tree(values)
        
        
        