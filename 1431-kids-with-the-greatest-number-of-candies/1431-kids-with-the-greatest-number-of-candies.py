class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        res = []
        for candy in candies:
            if(candy + extraCandies >= max_value):
                res.append(True)
            else:
                res.append(False)
        
        return res
        