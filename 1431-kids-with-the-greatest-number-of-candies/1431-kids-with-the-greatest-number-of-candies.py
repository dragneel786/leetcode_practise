class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        return [candy + extraCandies >= max_value for candy in candies]
        