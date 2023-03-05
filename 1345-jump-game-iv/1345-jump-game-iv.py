class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        imap = defaultdict(list)
        for i, a in enumerate(arr):
            imap[a].append(i)
        
        q = deque([0])
        steps = 0
        visited = set([0])
        n = len(arr)
        while(q):
            for _ in range(len(q)):
                idx = q.popleft()
                if(idx == n - 1):
                    return steps
                
                if(idx - 1 > 0 and\
                   idx - 1 not in visited):
                    # imap[arr[idx - 1]].popleft()
                    visited.add(idx - 1)
                    q.append(idx - 1)
                
                if(idx + 1 < n and\
                   idx + 1 not in visited):
                    # imap[arr[idx + 1]].popleft()
                    visited.add(idx + 1)
                    q.append(idx + 1)
                
                while(imap[arr[idx]]):
                    nidx = imap[arr[idx]].pop()
                    if(nidx not in visited):
                        visited.add(nidx)
                        q.append(nidx)
            
            steps += 1
        
        return steps
        
        