class Solution:
    def stringHash(self, s: str, k: int) -> str:
        
        size = len(s)
        # print(size, sub_size)
        res = []
        for i in range(0, size, k):
            val = 0
            for c in s[i: i + k]:
                val += ord(c) - 97
            
            val %= 26
            res.append(chr(97 + val))
        
        return ''.join(res)