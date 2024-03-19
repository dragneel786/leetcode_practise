class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = 0
        for i in range(len(s)):
            vows = cons = 0
            for j in range(i, len(s)):
                if(s[j] in vowels):
                    vows += 1
                else:
                    cons += 1
                
                if(vows == cons and (vows * cons) % k == 0):
                    ans += 1
            
        return ans
                
                
                