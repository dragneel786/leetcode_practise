class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        arr.append(-1)
        prev = ans = -1
        count = 0
        for a in arr:
            if(prev != a):
                if(count == prev):
                    ans = prev
                prev = a
                count = 0
            
            count += 1
        
        return ans
        