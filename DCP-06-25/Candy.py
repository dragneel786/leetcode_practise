class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        assign = [0] * n
        assign[0] = 1
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                assign[i] = assign[i - 1] + 1
            else:
                assign[i] = 1
 
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and assign[i] <= assign[i + 1]:
                assign[i] = assign[i + 1] + 1
        
        return sum(assign)
