class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        asum = sum(aliceSizes)
        needed = (asum + sum(bobSizes)) / 2
        bcounter = Counter(bobSizes)
        
        for a in aliceSizes:
            alice_needs = needed - (asum - a)
            if(alice_needs in bcounter): return [a, alice_needs]
        