class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        q = deque()
        q.append("0")
        q.append(num[0])
        for i in range(1, len(num)):
            while(k > 0 and len(q) > 0 and int(num[i]) < int(q[-1])):
                q.pop()
                k -= 1

            q.append(num[i])

        while(k):
            q.pop()
            k -= 1

        return str(int(''.join(q)))