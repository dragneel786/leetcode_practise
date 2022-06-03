class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        chars[s[0]] += 1
        
        index = count = 1
        maxCount = last = 0
        n = len(s)
        while(index < n):
            chars[s[index]] += 1
            count += 1
            
            if(count - chars[s[last]] > k):
                chars[s[last]] -= 1
                last += 1
                count -= 1
            
            maxCount = max(count, maxCount)
            index += 1
        
        if(count - chars[s[last]] < k):
            count += k
        
        return min(max(count, maxCount), n)