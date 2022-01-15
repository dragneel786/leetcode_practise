class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev = 1
        curr = 1
        for i in range(n - 1, -1, -1):
            res = 0
            if(s[i] != "0"):
                res = curr
                if(i < n - 1 and int(s[i: i + 2]) < 27):
                    res += prev

            prev = curr
            curr = res

        return curr