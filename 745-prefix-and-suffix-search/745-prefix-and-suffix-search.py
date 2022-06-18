class WordFilter:

    def __init__(self, words: List[str]):
        self.pre = dict()
        for k,w in enumerate(words):
            s = "#" + w
            for t in w[::-1]:
                s = t + s
                n, pre = len(s), self.pre
                for c in s:
                    pre[c] = pre.get(c, dict())
                    pre["$"] = pre.get("$", list())
                    pre["$"].append(k)
                    pre = pre[c]
                
                pre["$"] = pre.get("$", list())
                pre["$"].append(k)
        
    def f(self, prefix: str, suffix: str) -> int:
        pre = self.pre
        for c in suffix + "#" + prefix:
            if(c not in pre):
                return -1
            pre = pre[c]
        
        return pre["$"][-1]
        
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)