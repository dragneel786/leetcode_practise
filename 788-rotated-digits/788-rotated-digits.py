class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        s1 = set([2, 5, 6, 9])
        s2 = set([1, 8, 0])
        
        def is_valid(val):
            valid = False
            for c in str(val):
                v = int(c)
                if(v not in s1 and v not in s2):
                    return False
                valid = valid or v in s1
                
            return valid
        
        counts = 0
        for num in range(n + 1):
            counts += is_valid(num)
        
        return counts