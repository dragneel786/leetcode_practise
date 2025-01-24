class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        def is_possible(c):
            nonlocal wcounts
            for k in wcounts.keys():
                if k > c:
                    return False
            return True

        wcounts = Counter()
        max_size = 0
        start = 0
        for i, c in enumerate(word):
            while(not is_possible(c) and start < i):
                wcounts[word[start]] -= 1
                if wcounts[word[start]] == 0:
                    del wcounts[word[start]]
                
                start += 1

            wcounts[c] += 1
            if len(wcounts) == 5:
                max_size = max(max_size, i - start + 1)

        return max_size