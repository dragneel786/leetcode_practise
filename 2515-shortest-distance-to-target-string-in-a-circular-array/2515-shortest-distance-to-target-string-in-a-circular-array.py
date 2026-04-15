class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res = inf
        n = len(words)
        for i, word in enumerate(words):
            if word != target:
                continue
            
            if i < startIndex:
                res = min(startIndex - i, res)
                res = min((i - 0) + (n - startIndex), res)
            
            else:
                res = min(i - startIndex, res)
                res = min((n - i) + (startIndex - 0), res)

        return res if res != inf else -1