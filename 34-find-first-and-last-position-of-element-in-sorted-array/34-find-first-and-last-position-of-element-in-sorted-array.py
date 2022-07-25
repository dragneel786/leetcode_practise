class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def getDirection(mid):
            if(nums[mid] == target):
                return 0
            if(nums[mid] < target):
                return 1
            else:
                return -1
        
        n = len(nums)
        res = [-1, -1]
        ll = lr = 0
        hl = hr = n - 1
        while(ll <= hl or lr <= hr):
            if(ll <= hl):
                midl = ((hl - ll) >> 1) + ll
                d = getDirection(midl)
                res[0] = midl if(d == 0) else res[0]
                if(d == 1):
                    ll = midl + 1
                else:
                    hl = midl - 1
            
            if(lr <= hr):
                midr = ((hr - lr) >> 1) + lr
                d = getDirection(midr)
                res[1] = midr if(d == 0) else res[1]
                if(d == -1):
                    hr = midr - 1
                else:
                    lr = midr + 1
        
        return res
        