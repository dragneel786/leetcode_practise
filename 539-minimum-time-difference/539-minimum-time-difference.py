class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ans = []
        for t in timePoints:
            hm = t.split(":")
            mins = (60 * int(hm[0]) + int(hm[1]))
            ans.append(mins)
        
        ans.sort()
        res = math.inf
        for i in range(1, len(ans)):
            res = min(res, ans[i] - ans[i - 1])
            
        return min(res, (60 * 24) - ans[-1] + ans[0])