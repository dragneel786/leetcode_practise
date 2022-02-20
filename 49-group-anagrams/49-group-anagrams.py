class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = dict()
        for s in strs:
            tups = ''.join(sorted(s))
            if(tups in group):
                group[tups].append(s)
            else:
                group[tups] = [s]

        res = []
        for k in group.keys():
            res.append(group[k])

        return res