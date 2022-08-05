class Solution:
    def longestPalindrome(self, s: str) -> int:
        center = False
        length = 0
        for v in Counter(s).values():
            center = center or (v & 1) == 1
            length += v // 2
        return (length * 2) + center
                