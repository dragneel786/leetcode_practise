/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func bstToGst(root *TreeNode) *TreeNode {
    
    var incrementNode func(node *TreeNode, val int) int;
    
    incrementNode = func(node *TreeNode, val int) int {
        if node == nil {
            return val
        }
    
        var rightVal = incrementNode(node.Right, val)
        node.Val += rightVal
        return incrementNode(node.Left, node.Val)
    }
    
    incrementNode(root, 0)
    return root
}