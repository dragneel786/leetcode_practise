class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0, 1, 1, 2]
        pow2 = 2
        idx = 0
        for i in range(4, n + 1):
            if(2 ** pow2 == i):
                idx = 0
                pow2 += 1
            
            ans.append(ans[idx] + 1)
            idx += 1
        
        return ans[:n + 1]
                