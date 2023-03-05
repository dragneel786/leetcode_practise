class Solution:
    def minJumps(self, arr: List[int]) -> int:
        def add_to_queue(q, nodes):
            while(nodes):
                poped = nodes.pop()
                if(0 < poped < n and\
                   poped not in visited):
                    visited.add(poped)
                    q.append(poped)
        
        
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
                
                add_to_queue(q, [*imap[arr[idx]],\
                                 idx - 1, idx + 1])
                imap[arr[idx]] = []
            
            steps += 1

        
        