class Solution:
    def getMaximumConsecutive(self, A):
        res = 1
        for a in sorted(A):
            if a > res: break
            res += a
        return res
        