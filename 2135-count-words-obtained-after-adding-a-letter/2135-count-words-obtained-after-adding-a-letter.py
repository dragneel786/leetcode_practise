class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        starts = set()
        for s in startWords:
            starts.add("".join(sorted(s)))
        
        count = 0
        for t in targetWords:
            sub = "".join(sorted(t))
            for i in range(len(t)):
                if(sub[:i] + sub[i + 1:] in starts):
                    count += 1
                    break
                    
        return count
                