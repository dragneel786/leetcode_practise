class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        target = Counter()
        for c in p:
            target[c] += 1
        
        curr_size = j = 0
        window = Counter()
        ans = []
        for i, c in enumerate(s):
            window[c] += 1
            curr_size += 1
            
            while(window[c] > target[c]):
                window[s[j]] -= 1
                j += 1
                curr_size -= 1
            
            if(curr_size == n and window == target):
                ans.append(j)
            
        return ans
            
            
                