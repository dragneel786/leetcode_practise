class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        n = len(num1)
        for i in range(n - 1, -1, -1):
            temp = ""
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                val = int(num1[i]) * int(num2[j]) + carry
                temp = str(val % 10) + temp
                carry = val // 10

            if(carry):
                temp = str(carry) + temp

            temp += '0' * (n - 1 - i)
            ans += int(temp)

        return str(ans)