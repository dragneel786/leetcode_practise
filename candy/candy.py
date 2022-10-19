class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        rates = [1] * n
        candy = 1
        for i in range(1, n):
            if(ratings[i] > ratings[i - 1]):
                rates[i] = rates[i - 1] + 1
        
        candy = rates[-1]
        for i in range(n - 2, -1, -1):
            if(ratings[i] > ratings[i + 1]\
               and rates[i] <= rates[i + 1]):
                candy += 1
                rates[i] = candy
            else:
                candy = rates[i]
        
        return sum(rates)
        
            
            