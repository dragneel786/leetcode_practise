class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fmap = {}
        idx = 0
        for v in range(1, floor(sqrt(n)) + 1):
            if(n % v == 0):
                fmap[v] = idx
                fmap[n // v] = 1000 - idx
                idx += 1
            
        facts = list(sorted(fmap.keys(), key=lambda x:fmap[x]))
        print(facts)
        return facts[k - 1] if(len(facts) >= k) else -1
                