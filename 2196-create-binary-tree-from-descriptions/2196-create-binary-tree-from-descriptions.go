/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func createBinaryTree(descriptions [][]int) *TreeNode {
    var isParent = make(map[int]bool)
    var nodeMap = make(map[int]*TreeNode)
    for _, d := range descriptions {
        var parent, child, isLeft = d[0], d[1], d[2]
        
        if _, ok := nodeMap[child]; !ok {
            nodeMap[child] = &TreeNode{ child, nil, nil, }
        }
        
        if _, ok := nodeMap[parent]; !ok {
            nodeMap[parent] = &TreeNode{ parent, nil, nil, }
        }
        
        if isLeft == 1 {
            nodeMap[parent].Left = nodeMap[child]
        } else {
            nodeMap[parent].Right = nodeMap[child]
        }
        
        if _, ok := isParent[parent]; !ok {
            isParent[parent] = true
        }
        
        isParent[child] = false
    }
    for k, v := range isParent {
        if v == true {
            return nodeMap[k]
        }
    }
    
    return nil
}