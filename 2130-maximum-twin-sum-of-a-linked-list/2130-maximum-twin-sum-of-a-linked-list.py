# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head
        st = deque()
        while fast:
            st.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        print(st)
        ans = 0
        while st:
            v = slow.val
            ans = max(ans, v + st.pop())
            slow = slow.next
        return ans