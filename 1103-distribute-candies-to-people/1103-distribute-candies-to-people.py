class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        compute = lambda i, n: (i * n + 1) + (i * n + n)
        factor = (num_people / 2)
        c = 0
        val = factor * compute(c, num_people)
        while(val <= candies):
            c += 1
            candies -= val
            val = factor * compute(c, num_people)
        
        res = [0] * num_people
        for i in range(1, num_people + 1):
            for j in range(c):
                res[i - 1] += (num_people * j) + i
        
        i = 0
        while(candies):
            val = (num_people * c) + (i + 1)
            if(val > candies):
                res[i] += candies
                break
            res[i] += val
            candies -= val
            i += 1
        
        return list(map(int, res))
            
        
            