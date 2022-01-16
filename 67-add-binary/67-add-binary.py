class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = len(a)
        m = len(b)
        ans = ""
        if(n > m):
            b = ("0" * (n - m)) + b
        else:
            a = ("0" * (m - n)) + a
        carry = 0
        for i in range(max(n, m) - 1, -1, -1):
            res = int(a[i]) + int(b[i]) + carry
            carry = res // 2
            res %= 2
            ans = str(res) + ans

        if(carry):
            ans = str(carry) + ans 
        return ans