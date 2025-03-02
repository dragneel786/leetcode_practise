class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ans, i, j = 0, homePos[0], homePos[1]
        while i != startPos[0]:
            ans += rowCosts[i]
            i += -1 if i > startPos[0] else 1
        while j != startPos[1]:
            ans += colCosts[j]
            j += -1 if j > startPos[1] else 1
        return ans








    