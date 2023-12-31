class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        parsed_chars = dict()
        max_len = -1
        for i, c in enumerate(s):
            if(c in parsed_chars):
                max_len = max(i - parsed_chars[c] - 1, max_len)
                continue
            
            parsed_chars[c] = i
        
        return max_len