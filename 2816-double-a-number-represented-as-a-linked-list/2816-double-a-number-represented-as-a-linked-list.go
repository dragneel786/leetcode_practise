/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func doubleIt(head *ListNode) *ListNode {
    var prev *ListNode
    for head != nil {
        nxt := head.Next
        head.Next = prev
        prev = head
        head = nxt
    }
    
    var newHead *ListNode
    head = prev
    remain := 0
    for head != nil {
        sumVal := (head.Val + head.Val + remain)
        node := &ListNode{
            Val: sumVal % 10,
            Next: newHead,
        }
        newHead = node
        remain = sumVal / 10
        head = head.Next
    }
    
    if remain > 0 {
        node := &ListNode{
            Val: remain,
            Next: newHead,
        }
        newHead = node
    }
    
    return newHead
}