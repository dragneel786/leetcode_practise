func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
    var node *TreeNode
    _, node = getDeepest(root)
    return node
}

func getDeepest(node *TreeNode) (int32, *TreeNode) {
    if node == nil {
        return 0, nil
    }

    left, leftNode := getDeepest(node.Left)
    right, rightNode := getDeepest(node.Right)

    switch {
    case left == right:
        return left + 1, node
    case left > right:
        return left + 1, leftNode
    default:
        return right + 1, rightNode
    }
}
