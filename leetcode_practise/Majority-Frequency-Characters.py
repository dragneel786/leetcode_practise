class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counts = Counter(s)
        group = defaultdict(set)
        for k, v in counts.items():
            group[v].add(k)
        
        largest_k, res = 0, ""
        for value, grp in group.items():
            if len(res) > len(grp):
                continue
            
            if len(res) < len(grp):
                res = ''.join(grp)
                largest_k = value
            
            elif largest_k < value:
                largest_k = value
                res = ''.join(grp)
        
        return res

    
        

