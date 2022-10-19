class Solution:
    def candy(self, ratings: List[int]) -> int:
        def traverse(ratings, reverse):
            indexes = range(n - 2, -1, -1)\
            if(reverse) else range(1, n) 
            
            direc = 1 if(reverse) else -1
            for i in indexes:
                if(ratings[i] > ratings[i + direc] \
                   and rates[i] <= rates[i + direc]):
                    rates[i] = rates[i + direc] + 1
        
        n = len(ratings)
        rates = [1] * n
        traverse(ratings, False)
        traverse(ratings, True)
        
        return sum(rates)
        
            
            