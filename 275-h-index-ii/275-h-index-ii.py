class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        res = 0
        l = 0
        h = n - 1
        while(l <= h):
            m = (h - l) // 2 + l
            if(citations[m] >= (n - m)):
                res = (n - m)
                h = m - 1
            else:
                l = m + 1
        return res