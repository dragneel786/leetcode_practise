/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func smallestFromLeaf(root *TreeNode) string {
    var res string;
    smallestLeaf(root, "", &res)
    return res
}

func smallestLeaf(root *TreeNode, chars string, res *string){
    if root == nil{
        return
    }
    
    temp := string(97 + root.Val) + chars
    
    if root.Left == nil && root.Right == nil {
        if len(*res) == 0 {
            *res = temp
        } else {
           *res = smallestString(*res, temp) 
        }
        return
    }
    smallestLeaf(root.Left, temp, res)
    smallestLeaf(root.Right, temp, res)
}

func smallestString(str1, str2 string) string{
    for i, char := range str1 {
        if i >= len(str2) {
            return str2
        }
        
        if char < rune(str2[i]) {
            return str1
        } else if char > rune(str2[i]) {
            return str2
        }
    }
    
    if len(str1) < len(str2){
        return str1
    }
    return str2
}