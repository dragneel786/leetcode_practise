class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack = deque()
        
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            
            if(not stack or stack[-1][0] <= num):
                stack.append((num, i))
            
            else:
                node = idx = -1
                while(stack and stack[-1][0] > num):
                    node, idx = stack.pop()
                
                nums[idx], nums[i] = nums[i], nums[idx]
                nums[i + 1:] = sorted(nums[i + 1:])
                return
                
        nums.sort()