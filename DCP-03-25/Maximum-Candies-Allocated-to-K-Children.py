class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def is_possible(val):
            if val == 0:
                return True
            div_in_k = 0
            for candy in candies:
                div_in_k += (candy // val)
            return div_in_k >= k
        
        # Handle edge case where we can't give any candy
        if sum(candies) < k:
            return 0
            
        left, right = 1, max(candies)
        
        while left <= right:
            middle = left + (right - left) // 2
            if is_possible(middle):
                left = middle + 1
            else:
                right = middle - 1
        
        return right

        