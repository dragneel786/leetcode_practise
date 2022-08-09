class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        trees = {a:1 for a in arr}
        arr.sort()
        M = 10 ** 9 + 7
        for i, a in enumerate(arr):
            for b in arr[:i]:
                key = a / b
                if(key in trees):
                    trees[a] += trees[key] * trees[b]
        return sum(trees.values()) % M
            