# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        deps = defaultdict(lambda:[-1, -1])
        node_props = {-1: [0, 0]}
        
        def traverse(node, depth):
            nonlocal deps, node_props
            if not node:
                return 0
            
            left = traverse(node.left, depth + 1)
            right = traverse(node.right, depth + 1)
            
            max_h = max(left, right)
            node_props[node.val] = [max_h, depth] # height, depths
            
            if node_props[deps[depth][0]][0] <= max_h:
                deps[depth] = [node.val, deps[depth][0]]
            
            elif node_props[deps[depth][1]][0] <= max_h:
                deps[depth][1] = node.val
            
            return max_h + 1
        
        traverse(root, 0)
        # print(node_props)
        # print(deps)
        res = []
        for q in queries:
            _, d = node_props[q]
            
            if q != deps[d][0]:
                res.append(sum(node_props[deps[d][0]]))
            
            else:
                if deps[d][1] != -1:
                    res.append(sum(node_props[deps[d][1]]))
                
                else:
                    res.append(d - 1)
                
        return res