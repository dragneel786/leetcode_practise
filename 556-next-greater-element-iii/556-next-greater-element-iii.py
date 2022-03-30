class Solution:
    def nextGreaterElement(self, n: int) -> int:
        num = [i for i in str(n)]
        l = len(num)
        for i in range(l - 2, -1, -1):
            j = i + 1
            while(j < l):
                if(num[j] > num[i]):
                    num[j], num[i] = num[i], num[j]
                    n = int(''.join(num)) 
                    return n if n < 2 ** 31 else -1
                j += 1
            j = i + 1
            val = num[i]
            while(j < l and val > num[j]):
                num[j - 1] = num[j]
                j += 1
            j -= 1
            num[j] = val

        return -1