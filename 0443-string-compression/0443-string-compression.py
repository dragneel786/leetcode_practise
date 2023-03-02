class Solution:
    def compress(self, chars: List[str]) -> int:
        p = 0
        ch, c = chars[0], 0
        n = len(chars)
        chars.append('-')
        for char in chars:
            if(ch != char):
                chars[p] = ch
                if(c > 1):
                    for nc in str(c):
                        chars[p + 1] = str(nc)
                        p += 1
                
                p += 1
                c = 0
                ch = char
                
            c += 1
        
        return p
                
        
                