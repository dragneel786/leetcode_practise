class Solution:
    def largestGoodInteger(self, num: str) -> str:
        counts = Counter()
        ans = ""
        for i, v in enumerate(num):
            counts[v] += 1
            if i > 2:
                pv = num[i - 3]
                counts[pv] -= 1
                if(counts[pv] == 0):
                    del counts[pv]
            
            if len(counts) == 1 and counts[v] == 3 and (len(ans) == 0 or ans < (v * 3)):
                ans = (v * 3)
                
        return ans
