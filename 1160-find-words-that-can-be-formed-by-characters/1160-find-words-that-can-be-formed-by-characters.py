class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        ans = 0
        for w in words:
            wc = Counter(w)
            canMake = True
            for k in wc.keys():
                if(wc[k] > chars[k]):
                    canMake = False
                    break
            ans += len(w) if(canMake) else 0
        return ans
            