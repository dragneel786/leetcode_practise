class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_que = deque()
        target_que = deque()
        for i, (s, t) in enumerate(zip(start, target)):
            if s != '_':
                start_que.append((s, i))
            
            if t != '_':
                target_que.append((t, i))
        
        if len(start_que) != len(target_que):
            return False
        
        while(start_que):
            s, si = start_que.popleft()
            t, ti = target_que.popleft()
            if s != t or \
            (s == 'L' and si < ti) or \
            (t == 'R' and si > ti):
                return False
            
        return True