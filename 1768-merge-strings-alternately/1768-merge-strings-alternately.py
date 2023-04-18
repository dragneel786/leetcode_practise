class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        empty = lambda a: a if(a) else ''
        return ''.join([empty(a) + empty(b) \
                for a, b in zip_longest(word1, word2)])