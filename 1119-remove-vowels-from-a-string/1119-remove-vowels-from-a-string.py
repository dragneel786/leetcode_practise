class Solution:
    def removeVowels(self, s: str) -> str:
        return ''.join(filter(
            lambda c:c not in {'a', 'e', 'i', 'o', 'u'}, s))
                