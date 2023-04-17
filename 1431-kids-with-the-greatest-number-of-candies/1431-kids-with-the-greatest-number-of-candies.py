class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        return map(lambda candy: candy + extraCandies >= max_value,\
                 candies)