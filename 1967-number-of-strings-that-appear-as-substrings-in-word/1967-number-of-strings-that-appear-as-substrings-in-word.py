class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        n = len(word)
        sp = Counter(patterns)
        count = 0
        
        for i in range(1, n + 1):
            for j in range(n - i + 1):
                w = word[j: j + i]
                count += sp[w]
                del sp[w]
                
        return count