# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque(self.populate(root))
        self.leftmost = self.q.popleft()
        
    def insert(self, val: int) -> int:
        node = TreeNode(val)
        self.q.append(node)
        l = self.leftmost
        ret = l.val
        if(not l.left):
            l.left = node
        else:
            l.right = node
            self.leftmost = self.q.popleft()
        return ret
        

    def get_root(self) -> Optional[TreeNode]:
        return self.root
    
    def populate(self, root) -> list:
        q = deque([root])
        res = []
        while(q):
            node = q.popleft()
            if(node.left):
                q.append(node.left)
            
            if(node.right):
                q.append(node.right)
            else:
                res.append(node)
        return res


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()