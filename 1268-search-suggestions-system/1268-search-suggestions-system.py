class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def makeTrie():
            for w in products:
                t = trie
                for c in w:
                    t[c] = t.get(c, dict())
                    t = t[c]
                t["$"] = None
        
        def getThree(tie, s):
            if(len(three) == 3):
                return
            if("$" in tie):
                three.append(s)
                
            for i in range(26):
                ch = chr(97 + i)
                if(ch in tie):
                    getThree(tie[ch], s + ch)
                    
        trie = dict()
        makeTrie()
        res = []
        n = len(searchWord)
        p = ""
        for i,c in enumerate(searchWord):
            if(c not in trie):
                extras = [[]] * (n - i)
                res.extend(extras)
                break
            p += c
            three = []
            getThree(trie[c], p)
            res.append(three)
            trie = trie[c]
        
        return res