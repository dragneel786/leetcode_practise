class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0, 1]
        till = 4
        idx = 0
        for i in range(2, n + 1):
            res.append(res[idx] + 1)
            idx += 1
            if(i == till - 1):
                idx = 0
                till <<= 1
        
        return res[:n + 1]
        