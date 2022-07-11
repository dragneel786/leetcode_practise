class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        j = 0
        for i in range(len(nums)):
            while(q and q[-1] < nums[i]): q.pop()
            q.append(nums[i])
            if((i - j) == k - 1):
                res.append(q[0])
                if(nums[j] == q[0]): q.popleft()
                j += 1
        return res