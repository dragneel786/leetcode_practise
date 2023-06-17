class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        
        @lru_cache(None)
        def ways(prev, i):
            nonlocal n1, n2
            if(i >= n1):
                return 0
            
            ret = inf
            if(i == 0 or prev < arr1[i]):
                 ret = ways(arr1[i], i + 1)

            idx = bisect_right(arr2, prev)
            if(idx < n2):
                ret = min(ret, 1 + ways(arr2[idx], i + 1))
                   
            return ret
        
        n1, n2 = len(arr1), len(arr2)
        arr2.sort()
        ret = ways(-inf, 0)
        return ret if ret != inf else -1