# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inOrd = self.__inOrder(root)
        self.point = 0
        
    def next(self) -> int:
        val = self.inOrd[self.point]
        self.point += 1
        return val

    def hasNext(self) -> bool:
        if(len(self.inOrd) == self.point):
            return False
        return True
    
    def __inOrder(self, root):
        res = []
        if(not root):
            return res
        res.extend(self.__inOrder(root.left))
        res.append(root.val)
        res.extend(self.__inOrder(root.right))
        return res


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()