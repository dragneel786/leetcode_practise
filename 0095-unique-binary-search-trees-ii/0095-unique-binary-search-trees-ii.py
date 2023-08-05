# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        
        def create_tree(li):
            if(not li):
                return [None]
            
            nodes = []
            for i, node in enumerate(li):
                root = TreeNode(node)
                for left in create_tree(li[:i]):
                    for right in create_tree(li[i + 1:]):
                        root = TreeNode(node)
                        root.left = left
                        root.right = right
                        nodes.append(root)
            return nodes

        tree_list = [i for i in range(1, n + 1)]
        return create_tree(tree_list)
        