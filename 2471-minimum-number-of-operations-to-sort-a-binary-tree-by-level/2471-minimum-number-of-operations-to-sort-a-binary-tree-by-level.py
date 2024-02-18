# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def swaps(arr):
            index_dict = {value: index for index, value in enumerate(arr)}
            sorted_arr = sorted(arr)
            diff = 0
            for i, a in enumerate(sorted_arr):
                if(arr[i] != sorted_arr[i]):
                    idx = index_dict[sorted_arr[i]]
                    arr[i], arr[idx] = arr[idx], arr[i]
                    
                    index_dict[arr[idx]] = idx
                    diff += 1
                
            return diff
            
                
        q = deque([root])
        ans = 0
        while(q):
            curr = []
            for _ in range(len(q)):
                node = q.popleft()
                curr.append(node.val)
                if(node.left):
                    q.append(node.left)
                
                if(node.right):
                    q.append(node.right)
                
            ans += swaps(curr)
                
        return ans