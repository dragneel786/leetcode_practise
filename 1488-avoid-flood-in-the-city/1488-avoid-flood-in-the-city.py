class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full, res, zeros = {}, [-1 for _ in rains], []
        for i, r in enumerate(rains):
            if(not r):
                zeros.append(i)
                res[i] = 1
            elif(r not in full):
                full[r] = i
            else:
                j = bisect_left(zeros, full[r])
                if(j < len(zeros)):
                    full[r] = i
                    res[zeros[j]] = r
                    zeros.pop(j)
                else:
                    return []
        return res
                    