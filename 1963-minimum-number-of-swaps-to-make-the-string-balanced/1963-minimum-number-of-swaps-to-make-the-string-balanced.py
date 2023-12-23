class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        op = cl = steps = 0
        op_idx = n - 1
        s = list(s)
        for i in range(n):
            op += s[i] == '['
            cl += s[i] == ']'

            while(s[op_idx] != '['):
                op_idx -= 1

            if(s[i] == ']' and cl > op):
                steps += 1
                cl -= 1
                op += 1
                s[i], s[op_idx] = s[op_idx], s[i]

            if(i >= op_idx):
                break


        return steps
            