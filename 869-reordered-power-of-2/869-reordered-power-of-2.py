class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for perm in permutations(str(n)):
            if(perm[0] != '0' and bin(int(''.join(perm))).count('1') == 1):
                return True
            
            
            