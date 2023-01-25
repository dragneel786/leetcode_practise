class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        make = lambda w: Counter(w)
        curr = None
        ans = []
        for w in words:
            val = make(w)
            if(curr != val):
                ans.append(w)
                curr = val
        
        return ans