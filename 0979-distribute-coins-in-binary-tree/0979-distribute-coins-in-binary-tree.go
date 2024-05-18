/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func distributeCoins(root *TreeNode) int {
    var ops = 0
    disCoins(root, &ops)
    return ops
}

func disCoins(root *TreeNode, ops *int) int {
    if root == nil {
        return 0
    }
    
    var left = disCoins(root.Left, ops)
    var right = disCoins(root.Right, ops)
    // fmt.Println(left, right, root.Val, root.Val + left + right - 1)
    *ops += int(math.Abs(float64(left))) + int(math.Abs(float64(right))) 
    return root.Val + left + right - 1
}