class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        def validate(bits):
            if(not bits):
                return True

            if(bits[-1] == 0 and validate(bits[:-1])):
                return True

            if(len(bits) >= 2 and bits[-2] == 1\
               and validate(bits[:-2])):
                return True

            return False
        
        return validate(bits[:-1])
            
        
        