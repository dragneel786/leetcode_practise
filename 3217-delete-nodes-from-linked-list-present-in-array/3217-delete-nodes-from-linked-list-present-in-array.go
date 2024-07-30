/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func modifiedList(nums []int, head *ListNode) *ListNode {
    var numSet = make(map[int]bool)
    for _, num := range nums {
        numSet[num] = true
    }
    
    var temp, prev = &ListNode{ -1, head, }, head
    head, prev = temp, temp
    temp = temp.Next
    for temp != nil {
        if numSet[temp.Val] {
            temp = temp.Next
            prev.Next = temp
        } else {
            temp = temp.Next
            prev = prev.Next
        }
    }
    return head.Next
}