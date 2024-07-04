/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeNodes(head *ListNode) *ListNode {
    var curr, ret, prev = head, head, &ListNode{}
    head = head.Next
    curr.Next = nil
    for head != nil {
        if head.Val == 0 {
            prev.Next = curr
            curr.Next = nil
            prev = curr
            curr = head
        }
        curr.Val += head.Val
        head = head.Next
    }
    
    return ret
}