/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func evaluateTree(root *TreeNode) bool {
    if root.Val == 0 || root.Val == 1 {
        return root.Val == 1
    }
    
    var left = evaluateTree(root.Left)
    var right = evaluateTree(root.Right)
    
    var res = left || right
    if root.Val == 3 {
        res = left && right
    }
    
    return res
}