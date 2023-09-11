class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        for i, g in enumerate(groupSizes):
            groups[g].append(i)
        
        res = []
        for k, v in groups.items():
            if(k < len(v)):
                for i in range(0, len(v), k):
                    res.append(v[i: i + k])
            else:
                res.append(v)
        
        return res
                