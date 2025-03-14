class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def is_possible(val):
            div_in_k = 0
            for candy in candies:
                div_in_k += (candy // val)

            return div_in_k >= k


        left, right = 1, sum(candies) // k
        res = 0
        while(left <= right):
            middle = left + (right - left) // 2
            if is_possible(middle):
                res = middle
                left = middle + 1
            else:
                right = middle - 1
        
        return res

        