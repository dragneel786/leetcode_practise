class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        sh = defaultdict(lambda:[])
        for i,c in enumerate(s):
            sh[c].append(i)
        
        def isSub(w):
            i = 0
            for c in w:
                if(not sh[c]):
                    return False
                idx = bisect_left(sh[c], i)
                if(idx == len(sh[c])):
                    return False
                i = sh[c][idx] + 1
            return True
    
        res = []
        for w in dictionary:
            if(isSub(w)):
                if(not res):
                    res = [len(w), w]
                else:
                    res = [len(w), w] if(len(w) > res[0] or\
                                         (len(w) == res[0] and w < res[1])) else res
        return res[1] if res else ""
                    