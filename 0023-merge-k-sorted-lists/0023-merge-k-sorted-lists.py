# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class Node:
            def __init__(self, val, node):
                self.val = val
                self.node = node
            
            def __lt__(self, other):
                return self.val <= other.val
        
        heap = []
        for li in lists:
            if(li):
                heap.append(Node(li.val, li))
        heapify(heap)
        
        head = curr = ListNode()
        while(heap):
            node = heappop(heap).node
            curr.next = node
            curr = node
            if(node.next):
                node = node.next
                heappush(heap, Node(node.val, node))        
        return head.next