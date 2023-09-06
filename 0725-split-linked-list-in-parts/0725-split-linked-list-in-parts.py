# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = 0
        temp = head
        while(temp):
            temp = temp.next
            size += 1
        
        
        if(size <= k):
            res = []
            for _ in range(k):
                nxt = None
                if(head):
                    nxt = head.next
                    head.next = None
                
                res.append(head)
                head = nxt
        
        else:
            l, rem = size // k, size % k
            curr_count = 1
            res = [head]
            prev = head
            head = head.next
            while(head):
                if(curr_count == (l + (rem > 0))):
                    prev.next = None
                    prev = head
                    head = head.next
                    curr_count = 1
                    res.append(prev)
                    rem -= 1
                else:
                    curr_count += 1
                    prev = prev.next
                    head = head.next

        return res
                
        