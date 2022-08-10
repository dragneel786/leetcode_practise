class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        def valid_need(sp, ne):
            res = []
            for s, n in zip(sp, ne):
                if(n - s < 0): return ()
                res.append(n - s)
            return tuple(res)
        
        @lru_cache(None)
        def get_lowest_price(needs):
            nonlocal price, special
            if(not any(needs)):
                return 0

            res = sum(n * p for n, p in zip(needs, price))
            for s in special:
                updated_need = valid_need(s, needs)
                if(updated_need):
                    res = min(res, get_lowest_price(updated_need) + s[-1])

            return res
                    
        return get_lowest_price(tuple(needs))