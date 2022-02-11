class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while(target != 1 and maxDoubles):
            if(not (target & 1)):
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            count += 1
        
        if(target >= 2):
            count += target - 1
        
        return count