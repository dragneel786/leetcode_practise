/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNodes(head *ListNode) *ListNode {
  stack := list.New()
  for head != nil {
      for stack.Len() > 0 && 
      stack.Back().Value.(*ListNode).Val < head.Val{
          node := stack.Back()
          stack.Remove(node)
      }
      
      nxt := head.Next
      head.Next = nil
      stack.PushBack(head)
      head = nxt
  }
  
  head = &ListNode{
      Val: -1,
      Next: nil,
  }
  
  curr := head
  for stack.Len() > 0 {
      node := stack.Front()
      stack.Remove(node)
      curr.Next = node.Value.(*ListNode)
      curr = curr.Next
  }
  return head.Next
}