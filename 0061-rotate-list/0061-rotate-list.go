/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func rotateRight(head *ListNode, k int) *ListNode {
    if k == 0 || head == nil {
        return head
    }

    size := 0
    temp := head
    for temp != nil {
        size++
        temp = temp.Next
    }
    
    k %= size
    if k == 0 {
        return head
    }

    temp = head
    for range (size - k - 1) {
        temp = temp.Next
    }
    
    // fmt.Println(temp)
    newTemp := temp.Next
    temp.Next = nil
    temp = newTemp
    for newTemp.Next != nil {
        newTemp = newTemp.Next
    }

    newTemp.Next = head
    return temp
}