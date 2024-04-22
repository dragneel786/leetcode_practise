func reverseEvenLengthGroups(head *ListNode) *ListNode {
    count := 1
    temp := head
    var prevTail *ListNode
    for temp != nil {
        currHead := temp
        index := 1
        for i := 1; temp.Next != nil && i < count; i++ {
            temp = temp.Next
            index++
        }
        if index % 2 == 0 {
            nxt := temp.Next
            temp.Next = nil
            newHead, newTail := reverse(currHead)
            if prevTail != nil {
                prevTail.Next = newHead
            }
            newTail.Next = nxt
            temp = newTail
        }
        prevTail = temp
        temp = temp.Next
        count++
    }
    return head
}

func reverse(head *ListNode) (*ListNode, *ListNode) {
    var prev *ListNode
    curr := head
    for curr != nil {
        nxt := curr.Next
        curr.Next = prev
        prev = curr
        curr = nxt
    }
    return prev, head
}