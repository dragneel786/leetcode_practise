/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func balanceBST(root *TreeNode) *TreeNode {
    nodeVals := treeToList(root)
    return formTree(nodeVals)
}

func treeToList(root *TreeNode) []int {
    if root == nil {
        return []int{}
    }
    nodes := treeToList(root.Left)
    nodes = append(nodes, root.Val)
    nodes = append(nodes, treeToList(root.Right)...)
    return nodes
}

func formTree(vals []int) *TreeNode {
    size := len(vals)
    if size == 0 {
        return nil
    }
    mid := size / 2
    return &TreeNode {
        vals[mid],
        formTree(vals[:mid]),
        formTree(vals[mid + 1:]),
    }
}