# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def lca(leaves):
            while(len(set(leaves)) > 1):
                new_lea = []
                for node in leaves:
                    new_lea.append(node.parent)
                
                leaves = new_lea
            return leaves[0]

        q = deque([root])
        leafy = []
        while(q):
            curr_level = []
            for _ in range(len(q)):
                node = q.popleft()
                curr_level.append(node)
                if node.left:
                    q.append(node.left)
                    node.left.parent = node

                if node.right: 
                    q.append(node.right)
                    node.right.parent = node
            
            leafy = curr_level

        return lca(leafy)
