class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = dict()
        
        def get(s):
            alpha = [0] * 26
            for i in s:
                alpha[ord(i) - 97] += 1
    
            return tuple(alpha[:])
    
        for s in strs:
            tups = get(s)
            if(tups in group):
                group[tups].append(s)
            else:
                group[tups] = [s]

        res = []
        for k in group.keys():
            res.append(group[k])
        
        return res