class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        combine = Counter()
        for w in words2:
            combine |= Counter(w)
        return [w for w in words1 if not combine - Counter(w)]
    