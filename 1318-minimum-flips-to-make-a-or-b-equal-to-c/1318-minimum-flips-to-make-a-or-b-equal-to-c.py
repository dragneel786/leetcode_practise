class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while(a or b or c):
            if((c & 1) != ((a | b) & 1)):
                ans += 1
                if(a & 1 and b & 1):
                    ans += 1
            
            a >>= 1
            b >>= 1
            c >>= 1
            
        return ans
                
        