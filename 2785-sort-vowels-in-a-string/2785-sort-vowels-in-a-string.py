class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        vsort = []
        for c in s:
            if(c.lower() in vowels):
                vsort.append(c)
        
        vsort.sort()
        j = 0
        for i, c in enumerate(s):
            if(c.lower() in vowels):
                s[i] = vsort[j]
                j += 1
        
        return ''.join(s)