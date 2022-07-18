class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        ans = 0
        for w in words:
            wc = Counter(w)
            if(all(wc[k] <= chars[k] for k in wc.keys())):
                ans += len(w)
        return ans
            