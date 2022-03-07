class Solution:
    def countOdds(self, low: int, high: int) -> int:
        range = (high - low) + 1
        if(range % 2 == 0):
            return range // 2
        
        if(low % 2 == 1 and high % 2 == 1):
            return range // 2 + 1
    
        return range // 2 - 1 + 1