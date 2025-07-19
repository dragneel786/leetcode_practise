class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        def tvs(tri, curr = []):
            nonlocal res
            if "$" in tri:
                res.append("/" + '/'.join(curr))
                return
            
            for k in tri.keys():
                tvs(tri[k], curr + [k])


        trie = {}
        for fdr in folder:
            tmp = trie
            for c in fdr[1:].split("/"):
                if c == '/':
                    continue

                tmp.setdefault(c, {})
                tmp = tmp[c]
            
            tmp["$"] = 1
        
        res = []
        tvs(trie)
        return res