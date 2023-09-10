class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        
        slen = len(s)
        ans = [0] * slen
        
        q = deque()
        for i in range(slen):
            sr, sc = startPos
            state = [sr, sc, i, i]
            q.append(state)
        
        direc = {'L':(0,-1), 'R':(0,1), 'U':(-1,0), 'D':(1,0)}
        while(q):
            for _ in range(len(q)):
                sr, sc, start, curr = q.popleft()
                if(curr == slen):
                    ans[start] = curr - start
                    continue
                
                dr, dc = direc[s[curr]]
                nr, nc = sr + dr, sc + dc
                if(nr < 0 or nr >= n or nc < 0 or nc >= n):
                    ans[start] = curr - start
                    continue
                
                q.append([nr, nc, start, curr + 1])
        
        return ans
        