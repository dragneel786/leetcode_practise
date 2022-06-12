class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def isSub(w):
            i = 0
            for c in w:
                idx = bisect_left(indexes[c], i)
                if(idx == len(indexes[c])):
                    return False
                i = indexes[c][idx] + 1
            return True
                
        indexes = defaultdict(lambda:[])
        for i,ch in enumerate(source):
            indexes[ch].append(i)
        
        for c in target:
            if(not indexes[c]):
                return -1
        
        counts = 0
        n = len(source)
        m = len(target)
        i = 0
        while(i < m):
            w = n if(n < m - i) else m - i 
            while(not isSub(target[i: i + w])):
                w -= 1
            counts += 1
            i += w
        return counts