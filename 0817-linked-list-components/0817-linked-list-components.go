/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func numComponents(head *ListNode, nums []int) int {
    clusters, curr := 0, 0
    set := make(map[int]bool)
    
    for _, val := range nums {
        set[val] = true
    }
    
    for head != nil {
        if set[head.Val] {
            curr += 1
        } else {
            if(curr > 0) {
                clusters += 1
            }
            curr = 0
        }
        
        head = head.Next
    }
    
    if curr > 0 {
        clusters += 1
    }

    return clusters
}