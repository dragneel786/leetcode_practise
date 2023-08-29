class Solution:
    def bestClosingTime(self, customers: str) -> int:
        early = loss = inf
        new_y = Counter(customers)['Y']
        old_n = 0
        
        for i, c in enumerate(customers + '-'):
            if(loss > new_y + old_n):
                early = i
                loss = new_y + old_n
            
            old_n += c == 'N'
            new_y -= c == 'Y'
        
        return early
            
            
        