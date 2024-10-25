class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        def construct_trie():
            trie = dict()
            for f in folder:
                temp = trie
                for c in f[1:].split("/"):
                    temp.setdefault(c, [0, {}])
                    temp[c][0] += 1
                    temp = temp[c][1]
            
            return trie
        
        def traverse(tie, fc, val = ""):
            nonlocal res, folder
            if not tie:
                res.append(val)
                return
            
            for k in tie.keys():
                c, nxt_trie = tie[k]
                if c < fc and val in folder:
                    res.append(val)
                    return
                    
                traverse(nxt_trie, c, val + '/' + k)             
                
            
        trie = construct_trie()
        folder = set(folder)
        res = []
        traverse(trie, 0)        
        return res