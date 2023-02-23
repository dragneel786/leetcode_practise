# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        val_node = {}
        parent = set()
        child = set()
        for p, c, isleft in descriptions:
            val_node[p] = val_node.get(p, TreeNode(p))
            val_node[c] = val_node.get(c, TreeNode(c))
            
            if(isleft):
                val_node[p].left = val_node[c]
            else:
                val_node[p].right = val_node[c]
            
            parent.add(p)
            child.add(c)
        
        
        return val_node[list(parent - child)[0]]