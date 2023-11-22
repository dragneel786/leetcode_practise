class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        q = deque([(0, 0)])
        while(q):
            row, col = q.popleft()
            ans.append(nums[row][col])
            
            if(col == 0 and row + 1 < len(nums)):
                q.append((row + 1, col))
            
            if(col + 1 < len(nums[row])):
                q.append((row, col + 1))
        
        return ans
        