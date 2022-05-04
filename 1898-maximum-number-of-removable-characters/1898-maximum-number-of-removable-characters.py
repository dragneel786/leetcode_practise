class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        low = 0
        high = len(removable)
        
        def isSubSeq(st):
            i = 0
            j = 0
            while(i < len(st)):
                if(st[i] == p[j]):
                    j += 1
                if(j == len(p)):
                    return True
                i += 1
            
            return False
        
        res = 0
        while(low <= high):
            mid = (high - low) // 2 + low
            temp = list(s)
            for j in range(mid):
                temp[removable[j]] = "_"
            if(isSubSeq(temp)):
                low = mid + 1
                res = mid
            else:
                high = mid - 1
        return res