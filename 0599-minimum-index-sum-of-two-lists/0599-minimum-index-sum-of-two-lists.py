class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        imap = {s: i for i, s in enumerate(list1)}
        res = []
        for i, s in enumerate(list2):
            if(s in imap):
                res.append((i + imap[s], s))
        
        c = -1
        if(res):
            res.sort()
            c = res[0][0]
        
        return [s for count, s in res if(count == c)]
    
            
                
            
            
            