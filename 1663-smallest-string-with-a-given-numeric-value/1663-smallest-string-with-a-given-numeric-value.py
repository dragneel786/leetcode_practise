class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = []
        for _ in range(k // 26):
            ans.append("z")
        if(k % 26):
            ans.append(chr(k % 26 + 96))

        rem = n - len(ans)
        if(rem > 0):
            temp = rem
            pos = -1
            while(temp):
                if(ord(ans[pos]) - 96 == 1):
                    pos += -1
                ans[pos] = chr(ord(ans[pos]) -1)
                temp -= 1

            ans.append("a" * rem)
        return "".join(ans)[::-1]