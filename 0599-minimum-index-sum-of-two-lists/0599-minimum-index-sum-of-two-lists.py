class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        imap = {s: i for i, s in enumerate(list1)}
        res = defaultdict(list)
        count = inf
        for i, s in enumerate(list2):
            if(s in imap):
                c = imap[s] + i
                res[c].append(s)
                count = min(c, count)
        
        return res[count]
        
    
            
                
            
            
            