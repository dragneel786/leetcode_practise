/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func nodesBetweenCriticalPoints(head *ListNode) []int {
    var prev, curr = head, head.Next
    var idxs = []int{}
    var index = 1
    for curr.Next != nil {
        if prev.Val < curr.Val && curr.Val > curr.Next.Val {
            idxs = append(idxs, index)
        }
        
        if prev.Val > curr.Val && curr.Val < curr.Next.Val {
            idxs = append(idxs, index)
        }
        index++
        prev = curr
        curr = curr.Next
    }
    
    var res = []int{-1, -1}
    if len(idxs) < 2 { return res }
    
    res[0] = math.MaxInt
    res[1] = idxs[len(idxs) - 1] - idxs[0]
    for i := range len(idxs) - 1 {
        res[0] = min(res[0], idxs[i + 1] - idxs[i])
    }
    return res
}