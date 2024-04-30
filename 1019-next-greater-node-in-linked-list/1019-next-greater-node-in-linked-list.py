# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        n = 0
        temp = head
        while(temp != None):
            n += 1
            temp = temp.next
            
        answer = [0] * n
        i = 0
        st = deque()
        while(head):
            while(st and st[-1][0] < head.val):
                _, idx = st.pop()
                answer[idx] = head.val
            
            st.append((head.val, i))
            i += 1
            head = head.next
        
        return answer
        
        