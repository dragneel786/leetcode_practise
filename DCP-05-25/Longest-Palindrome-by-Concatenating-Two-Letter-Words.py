class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = single = 0
        counts = Counter(words)
        for word in words:
            rev_word = word[::-1]
            if word == rev_word and counts[word] >= 1:
                single += 1
                if counts[word] >= 2:
                    res += 4
                    single -= 1
                    counts[word] -= 2

            elif counts[word] >= 1 and counts[rev_word] >= 1:
                res += 4
                counts[word] -= 1
                counts[rev_word] -= 1

        return res + ((single > 0) * 2)