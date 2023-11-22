class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = []
        low, high = 0, len(s)
        for c in s:
            if(c == 'I'):
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1
        
        ans.append(low)
        return ans