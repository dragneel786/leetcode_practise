class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pCnt = nCnt = lastPcnt = firstPcnt = 0
        ans = 0
        nums.append(0)
        for num in nums:
            if num == 0:
                if (nCnt % 2 == 0):
                    ans = max(ans, pCnt + nCnt)
                else:
                    # print("pCnt = {}, nCnt = {}, firstPcnt = {}, lastPcnt = {}".format(pCnt, nCnt, firstPcnt, lastPcnt))
                    ans = max(ans, pCnt - min(firstPcnt, lastPcnt) + nCnt - 1)
                firstPcnt = lastPcnt = pCnt = nCnt = 0
            elif num < 0:
                nCnt += 1
                lastPcnt = 0
            else:
                if nCnt == 0:
                    firstPcnt += 1
                pCnt += 1
                lastPcnt += 1
        return ans