class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        target = [0] * 26
        for c in p:
            target[ord(c) - 97] += 1
        
        window = [0] * 26
        ans = []
        for i, c in enumerate(s):
            ci = ord(c) - 97
            window[ci] += 1
            if(i >= n):
                window[ord(s[i - n]) - 97] -= 1
                
            if(window == target):
                ans.append((i - n + 1))
            
        return ans
            
            
                