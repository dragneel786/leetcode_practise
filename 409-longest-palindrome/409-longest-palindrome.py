class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        is_one = False
        length = 0
        for v in counter.values():
            if(v & 1):
                is_one = True
            
            length += v // 2
        
        return (length * 2) + is_one
                