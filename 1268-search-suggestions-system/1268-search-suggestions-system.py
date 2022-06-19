class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        def makeTrie():
            for w in products:
                t = trie
                for c in w:
                    t[c] = t.get(c, dict())
                    t[c][3] = t[c].get(3, list())
                    if(len(t[c][3]) < 3) :
                        t[c][3].append(w)
                    t = t[c]
                
        trie = dict()
        makeTrie()
        res = []
        empty = False
        for c in searchWord:
            if(c not in trie or empty):
                empty = True
                res.append([])
                continue
            res.append(trie[c][3])
            trie = trie[c]
            
        
        
        return res