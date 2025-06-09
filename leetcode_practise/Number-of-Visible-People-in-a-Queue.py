class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            count = 0
            h = heights[i]
            while stack and stack[-1] < h:
                stack.pop()
                count += 1
            if stack:
                count += 1
            res[i] = count
            stack.append(h)
        return res