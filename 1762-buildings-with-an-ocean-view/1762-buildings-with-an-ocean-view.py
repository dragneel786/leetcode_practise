class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = deque()
        maxh = -1
        for i in range(len(heights) - 1, -1, -1):
            if(maxh < heights[i]):
                ans.appendleft(i)
                maxh = heights[i]
            
        return ans