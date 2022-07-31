class Node:
    def __init__(self, val = 0, start = -1, end = -1, left = None, right = None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right
    
class NumArray:

    def __init__(self, nums: List[int]):
        def buildTree(low, high):
            if(low == high):
                return Node(nums[low], low, high)
            
            mid = ((high - low) // 2) + low
            newNode = Node(0, low, high)
            newNode.left = buildTree(low, mid)
            newNode.right = buildTree(mid + 1, high)
            newNode.val = newNode.left.val + newNode.right.val
            return newNode
        
        self.root = buildTree(0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        def updateValue(root, index, val):
            if(index == root.start == root.end):
                root.val = val
                return 
            
            mid = (root.start + root.end) // 2
            if(index <= mid):
                updateValue(root.left, index, val)
            else:
                updateValue(root.right, index, val)
            root.val = root.left.val + root.right.val
                
        updateValue(self.root, index, val)
        
    def sumRange(self, left: int, right: int) -> int:
        def sumRangeValue(root, left, right):
            if(not root):
                return 0
            
            if(root.start == left and root.end == right):
                return root.val
            
            mid = (root.start + root.end) // 2
            ret = 0
            if(left <= mid):
                ret += sumRangeValue(root.left, left, min(mid, right))
            
            if(right > mid):
                ret += sumRangeValue(root.right, max(mid + 1, left), right)
            
            return ret
    
        return sumRangeValue(self.root, left, right)