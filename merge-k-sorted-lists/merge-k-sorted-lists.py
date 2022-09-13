# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node:
    def __init__(self, val, point):
        self.val = val
        self.point = point
    
    def __lt__(self, other):
        return self.val < other.val or False

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for l in lists:
            if(l):
                heap.append(Node(l.val, l.next))
        
        heapify(heap)
        new_head = ListNode()
        temp = new_head
        while(heap):
            node = heappop(heap)
            temp.next = ListNode(node.val)
            
            if(node.point):
                heappush(heap, Node(node.point.val, node.point.next))
            
            temp = temp.next
        
        return new_head.next
            