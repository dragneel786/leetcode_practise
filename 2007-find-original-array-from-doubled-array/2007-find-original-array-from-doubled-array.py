class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if(n & 1): return []
        
        changed.sort()
        original = []
        # [1, 3, 4, 2, 6, 8]
        # [1, 2, 3, 4, 6, 8]
        dvalue = deque()
        for v in changed:
            if(dvalue and dvalue[0] == v / 2):
                original.append(
                    dvalue.popleft())
                continue
            
            dvalue.append(v)
            
        
        return original if(not dvalue) else []
            
        
        
            
            
            
        