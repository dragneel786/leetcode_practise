class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if("0000" in deadends):
            return -1
        visited = set(deadends)
        visited.add("0000")
        q = deque([("0000", 0)])
        fw = {'0':'1', '1':'2', '2':'3', '3':'4',\
              '4':'5', '5':'6', '6':'7', '7':'8', '8':'9', '9':'0'}
        bw = {'0':'9', '1':'0', '2':'1', '3':'2', '4':'3', '5':'4',\
              '6':'5', '7':'6', '8':'7', '9':'8'}
        while(q):
            for _ in range(len(q)):
                slot, steps = q.popleft()
                if(slot == target):
                    return steps
                
                for i in range(4):
                    f = slot[:i] + fw[slot[i]] + slot[i + 1:]
                    b = slot[:i] + bw[slot[i]] + slot[i + 1:]
                    if(f not in visited):
                        visited.add(f)
                        q.append((f, steps + 1))
                    if(b not in visited):
                        visited.add(b)
                        q.append((b, steps + 1))
        return -1
                        
                
                
        