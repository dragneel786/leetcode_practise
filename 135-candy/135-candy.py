class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if(n == 1): return 1
        candies = [1] * len(ratings)
        for i in range(1, n):
            if(ratings[i - 1] < ratings[i]):
                candies[i] = candies[i - 1] + 1
        
        tot = candies[-1]
        for i in range(n - 2, -1, -1):
            if(ratings[i] > ratings[i + 1]\
               and candies[i] <= candies[i + 1]):
                candies[i] = candies[i + 1] + 1
            tot += candies[i]
        return tot