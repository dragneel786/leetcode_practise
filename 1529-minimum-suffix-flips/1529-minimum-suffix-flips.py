class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        end = n - 1
        while(end > -1 and target[end] == '1'):
            end -= 1
            
        ans = int(end != (n - 1))
        while(True):
            while(end > -1 and target[end] == '0'):
                end -= 1
            
            if(end < 0):
                break
            
            while(end > -1 and target[end] == '1'):
                end -= 1
            
            ans += 2
            
        return ans
        