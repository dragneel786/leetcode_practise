/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
    return rowAddedTree(root, val, depth, true)
}

func rowAddedTree(node *TreeNode, val int, depth int, isLeft bool) *TreeNode {
    if depth == 1 {
        newNode := &TreeNode{Val: val}
        
        if isLeft {
            newNode.Left = node
            return newNode
        }
        
        newNode.Right = node
        return newNode
    }
    if node != nil {
        node.Left = rowAddedTree(node.Left, val, depth-1, true)
        node.Right = rowAddedTree(node.Right, val, depth-1, false)
    }
    return node
}
