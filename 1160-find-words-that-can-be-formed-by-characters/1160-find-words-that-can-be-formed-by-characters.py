class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counts = Counter(chars)
        return sum([len(word) for word in words if(not Counter(word) - char_counts)])