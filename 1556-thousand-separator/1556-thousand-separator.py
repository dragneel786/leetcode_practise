class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        ans = deque()
        for i in range(len(n), 0, -3):
            till = i - 3 if(i - 3 > 0) else 0
            ans.appendleft(n[till: i])
        

        return '.'.join(ans)