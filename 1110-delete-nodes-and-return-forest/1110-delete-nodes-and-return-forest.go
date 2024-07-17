/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
    var delMap = make(map[int]bool)
    for _, val := range to_delete {
        delMap[val] = true
    }
    
    var treeRoots = [](*TreeNode){}
    var pOrder func(node *TreeNode) *TreeNode;
    pOrder = func(node *TreeNode) *TreeNode {
        if node == nil{ return nil}
        
        node.Left = pOrder(node.Left)
        node.Right = pOrder(node.Right)
        if delMap[node.Val] {
            if node.Left != nil {treeRoots = append(treeRoots, node.Left)}
            if node.Right != nil {treeRoots = append(treeRoots, node.Right)}
            return nil
        }
        return node
    }
    var dummyRoot = &TreeNode{-1, root, nil,}
    pOrder(dummyRoot)
    if dummyRoot.Left != nil {treeRoots = append(treeRoots, dummyRoot.Left)}
    return treeRoots
}