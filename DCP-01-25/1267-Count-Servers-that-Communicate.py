# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(0, head)
        temp = head
        curr_sum = 0
        seen_so_far = set([0])
        q = deque([(0, new_head)])
        while(temp):
            curr_sum += temp.val
            if(curr_sum in seen_so_far):
                while(q and q[-1][0] != curr_sum):
                    val, _ = q.pop()
                    seen_so_far.remove(val)
                    
                q[-1][1].next = temp.next
            
            else:
                q.append((curr_sum, temp))
                seen_so_far.add(curr_sum)
                
            temp = temp.next
                
        return new_head.next