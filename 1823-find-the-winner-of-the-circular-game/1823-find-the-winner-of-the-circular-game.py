class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # from collections import deque
        q = deque([i for i in range(1, n + 1)])
        while len(q) > 1:
            for _ in range(k - 1):
                q.append(q.popleft())

            q.popleft()
            # print(q)

        return q.popleft()

        
        