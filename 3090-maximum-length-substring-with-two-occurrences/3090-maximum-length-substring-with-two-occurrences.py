class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = length = start = 0
        counts = Counter()
        for i, c in enumerate(s):
            while(counts[c] > 1):
                counts[s[start]] -= 1
                start += 1

            counts[c] += 1
            max_len = max(max_len, i - start + 1)

        return max_len