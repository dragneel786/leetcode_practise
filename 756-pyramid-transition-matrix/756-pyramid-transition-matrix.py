class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        suf = defaultdict(lambda:[])
        for a in allowed:
            suf[a[:2]].append(a[2])
        
        def dfs(bottom):
            n = len(bottom)
            if(n == 2 and bottom in suf):
                return True
            options = []
            for i in range(n - 1):
                chs = bottom[i: i + 2]
                if(chs in suf):
                    options.append(suf[chs])
                else:
                    return False
            for p in itertools.product(*options):
                if(dfs(''.join(p))):
                    return True
            return False
        
        return dfs(bottom)
                        
                        