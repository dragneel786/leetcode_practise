# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        
        def popper(node, leftToRight):
            ret = [node.left, node.right]
            return ret if(leftToRight) else ret[::-1]
            
        st = deque([root])
        l = 0
        res = []
        while(st):
            tempQ = deque()
            tempL = deque()
            for _ in range(len(st)):
                node = st.pop()
                tempL.appendleft(node.val)
                for child in popper(node, l & 1):
                    if(child):
                        tempQ.append(child)
            l += 1
            res.append(tempL)
            st = tempQ
            
        return res
                
                    
                    
            
            
        
        