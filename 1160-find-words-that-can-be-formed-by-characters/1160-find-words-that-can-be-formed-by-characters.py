class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans, chars = 0, Counter(chars)
        for w in words:
            wc = Counter(w)
            for k in wc.keys():
                if(wc[k] > chars[k]):
                    break
            else:
                ans += len(w)  
        return ans
            