class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        target = [0] * 26
        for c in p:
            target[ord(c) - 97] += 1
        
        curr_size = j = 0
        window = [0] * 26
        ans = []
        for i, c in enumerate(s):
            ci = ord(c) - 97
            window[ci] += 1
            curr_size += 1
            
            while(window[ci] > target[ci]):
                cj = ord(s[j]) - 97
                window[cj] -= 1
                j += 1
                curr_size -= 1
            
            if(curr_size == n and window == target):
                ans.append(j)
            
        return ans
            
            
                