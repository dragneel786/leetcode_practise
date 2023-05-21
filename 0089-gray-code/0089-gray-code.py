class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0, 1]
        pows = 2
        for _ in range(1, n):
            extra = []
            for i in range(pows):
                extra.append(ans[i] + pows)
            
            pows *= 2
            ans.extend(extra[::-1])
            
        return ans
        