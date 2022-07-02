class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        maxH = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            maxH = max(maxH, horizontalCuts[i] - horizontalCuts[i - 1])
        
        maxV = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            maxV = max(maxV, verticalCuts[i] - verticalCuts[i - 1])
        
        return (maxH * maxV) % ((10 ** 9 + 7))