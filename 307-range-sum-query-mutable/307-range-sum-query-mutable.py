class Node:
    def __init__(self, val = 0, start = -1, end = -5, left = None, right = None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right
        
class NumArray:

    def __init__(self, nums: List[int]):
        
        def buildTree(nums, start, end):
            if(start > end):
                return None
            
            if(start == end):
                return Node(nums[start], start, end)
            
            newNode = Node()
            mid = (end - start) // 2 + start
            newNode.left = buildTree(nums, start, mid)
            newNode.right = buildTree(nums, mid + 1, end)
            newNode.val = newNode.left.val + newNode.right.val
            newNode.start, newNode.end = start, end
            return newNode
        
        self.root = buildTree(nums, 0, len(nums) - 1)
            
    def update(self, index: int, val: int) -> None:
        def updateVal(root):
            if(root.start == root.end == index):
                root.val = val
                return
            
            mid = (root.end - root.start) // 2 + root.start
            if(index <= mid):
                updateVal(root.left)
            else:
                updateVal(root.right)
            root.val = root.left.val + root.right.val
        
        updateVal(self.root)

    def sumRange(self, left: int, right: int) -> int:
        def getSumRange(root, left, right):
            if(root.start == left and root.end == right):
                return root.val
            
            mid = (root.end - root.start) // 2 + root.start
            if(right <= mid):
                return getSumRange(root.left, left, right)
            elif(left > mid):
                return getSumRange(root.right, left, right)
            else:
                return getSumRange(root.left, left, mid) + \
            getSumRange(root.right, mid + 1, right)
        
        return getSumRange(self.root, left, right)
    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)