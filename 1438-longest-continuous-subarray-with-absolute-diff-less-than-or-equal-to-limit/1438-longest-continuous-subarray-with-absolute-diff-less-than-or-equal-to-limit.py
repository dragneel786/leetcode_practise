class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mn = deque()
        mx = deque()
        i = 0
        for a in nums:
            while(mn and mn[-1] > a): mn.pop()
            while(mx and mx[-1] < a): mx.pop()
            mn.append(a)
            mx.append(a)
            if(mx[0] - mn[0] > limit):
                if(mx[0] == nums[i]): mx.popleft()
                if(mn[0] == nums[i]): mn.popleft()
                i += 1
        return len(nums) - i
                
            