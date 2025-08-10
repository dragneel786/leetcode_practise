class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 1:
            return True 

        counts = Counter(str(n))
        val = 1
        for i in range(32):
            val <<= 1
            if counts == Counter(str(val)):
                return True
        
        return False