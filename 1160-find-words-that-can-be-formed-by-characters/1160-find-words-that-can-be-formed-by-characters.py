class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counts = Counter(chars)
        ans = 0
        for word in words:
            remain = len(Counter(word) - char_counts)
            if(not remain):
                ans += len(word)
        return ans