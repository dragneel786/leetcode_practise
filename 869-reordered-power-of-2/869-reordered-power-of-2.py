class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        counts = Counter(str(n))
        for i in range(31):
            num = 1 << i
            if(counts == Counter(str(num))):
                return True
            
            
            