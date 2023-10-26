class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        hset = Counter(arr)
        arr.sort()
        for i, a in enumerate(arr):
            for b in arr[:i + 1]:
                div = 1 if(a == b) else 2
                if(a * b in hset):
                    hset[a * b] += (div * hset[a] * hset[b])
        
        # print(hset)
        return sum(hset.values()) % (10 ** 9 + 7)
        