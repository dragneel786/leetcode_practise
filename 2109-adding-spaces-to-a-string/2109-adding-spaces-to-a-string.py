class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        string = []
        si = spi = 0
        while(spi < len(spaces)):
            if si == spaces[spi]:
                string.append(" ")
                spi += 1
            
            string.append(s[si])
            si += 1
            
        string.append(s[si:])
        return ''.join(string)
    