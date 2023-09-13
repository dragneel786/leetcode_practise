class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [1]
        for i in range(1, len(ratings)):
            if(ratings[i] <= ratings[i - 1]):
                ans.append(1)
            else:
                ans.append(ans[-1] + 1)
        
        for i in range(len(ratings) - 2, -1, -1):
            if(ratings[i] > ratings[i + 1] \
               and ans[i] <= ans[i + 1]):
                ans[i] = ans[i + 1] + 1
        
        return sum(ans)