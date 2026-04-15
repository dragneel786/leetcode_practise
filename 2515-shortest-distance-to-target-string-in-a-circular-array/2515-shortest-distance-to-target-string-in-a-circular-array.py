class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res = inf
        n = len(words)
        for i, word in enumerate(words):
            if word != target:
                continue
            
            res = min(res, abs(i - startIndex), n - abs(i - startIndex))

        return res if res != inf else -1