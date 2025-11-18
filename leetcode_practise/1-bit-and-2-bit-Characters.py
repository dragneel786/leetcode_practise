class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n, i = len(bits), 0
        single = True
        while(i < n):
            if bits[i] == 1:
                i += 2
                single = False
            else:
                i += 1
                single = True
        
        return single