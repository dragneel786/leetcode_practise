class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        que = deque()
        ans = []
        l = 0
        for i, num in enumerate(nums):
            while(que and nums[que[-1]] < num):
                que.pop()
            que.append(i)
            
            if(l > que[0]):
                que.popleft()
            
            if(i + 1 >= k):
                ans.append(nums[que[0]])
                l += 1
                
        return ans
        
        
    
        