class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        que = deque(range(len(s) + 1))
        res = [que.popleft() if(c == 'I')\
               else que.pop() for c in s]
        res.append(que.pop())
        return res
            