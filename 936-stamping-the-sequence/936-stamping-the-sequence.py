class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def is_replaceable(start):
            for j, ch in enumerate(stamp):
                if('?' != target[start + j] != ch):
                    return False
            return True   

        
        def replace(start):
            nonlocal count
            for j in range(stamp_size):
                if(target[start + j] != '?'):
                    count += 1
                    target[start + j] = '?'
                    
        
        count = 0
        target_size = len(target)
        stamp_size = len(stamp)
        
        target = list(target)
        visited = [False] * target_size
        res = []
        
        while(count < target_size):
            
            has_changed = False
            for i in range(target_size - stamp_size + 1):
                if(not visited[i] and is_replaceable(i)):
                    visited[i] = True
                    has_changed = True
                    replace(i)
                    res.append(i)
            
            if(not has_changed):
                return []
        
        return res[::-1]
        
            