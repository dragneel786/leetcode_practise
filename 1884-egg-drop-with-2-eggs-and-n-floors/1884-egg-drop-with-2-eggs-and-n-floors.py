class Solution:
    def twoEggDrop(self, n: int) -> int: 
        
        @lru_cache(None)
        def get_res(floor, egg = 2):
            if(floor in [0, 1] or egg == 1):
                return floor

            min_res = inf
            for k in range(1, floor + 1):
                temp = 1 + max(get_res(floor - k, egg),\
                               get_res(k - 1, egg - 1))

                min_res = min(min_res, temp)

            return min_res

        return get_res(n)