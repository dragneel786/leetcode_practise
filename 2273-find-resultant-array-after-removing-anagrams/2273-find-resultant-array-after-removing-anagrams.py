class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        return [next(w) for _,w in groupby(words, sorted)]