# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        def create_parent(node, parent = None):
            if(not node):
                return
            
            node.parent = parent
            create_parent(node.left, node)
            create_parent(node.right, node)
            
            
        def find_leaf(node):
            nonlocal ans
            if(not node):
                return
            
            if(not node.left and not node.right):
                dmap.clear()
                find_node(node)
                ans += len(dmap) - 1
            else:
                find_leaf(node.left)
                find_leaf(node.right)
        
        
        def find_node(node, dis = 0):
            nonlocal distance, ans
            if(dis > distance or not node):
                return
            
            
            if(not node.left and not node.right):
                dmap.add(id(node))
            
            find_node(node.left, dis + 1)
            find_node(node.right, dis + 1)
            find_node(node.parent, dis + 1)
            
                
        ans = 0
        dmap = set()
        create_parent(root)
        find_leaf(root)
        return ans // 2
        
        
            
            
            
            