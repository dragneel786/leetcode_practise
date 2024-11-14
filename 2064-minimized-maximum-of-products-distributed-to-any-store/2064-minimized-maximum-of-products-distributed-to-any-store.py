class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def allocalable(val):
            nonlocal n
            counts = 0
            for q in quantities:
                counts += (q // val) + (q % val > 0)
            # print(counts, val)
            return counts <= n
        
        
        low = 1
        high = max(quantities) + 1
        ans = high
        while(low <= high):
            mid = low + ((high - low) // 2)
            if allocalable(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return low
            