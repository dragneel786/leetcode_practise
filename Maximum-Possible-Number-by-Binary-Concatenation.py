class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def is_prefix(s1, s2):
            m, n = len(s1), len(s2)
            if m <= n:
                return s1 == s2[:m] and s1[::-1] == s2[n - m:][::-1]
            
            return False

        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                count += is_prefix(words[i], words[j])
        
        return count
                