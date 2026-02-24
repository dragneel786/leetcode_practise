/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumRootToLeaf(root *TreeNode) int {
    tot := 0
    pathSum(root, 0, &tot)
    return tot
}

func pathSum(node *TreeNode, val int, tot *int) {
    if node == nil {
        return
    }

    val = (val << 1) + node.Val
    if node.Left == nil && node.Right == nil {
        *tot += val
        return
    }
    pathSum(node.Left, val, tot)
    pathSum(node.Right, val, tot)
}