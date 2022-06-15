class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordSet = set(words)
        words.sort(key=lambda x: -len(x))
        length = defaultdict(lambda:1)
        maxChain = 1
        for w in words:
            for i in range(len(w)):
                term = w[0:i] + w[i + 1:]
                if(term in wordSet):
                    length[term] = max(length[term], length[w] + 1)
                    maxChain = max(length[term], maxChain)
        
        return maxChain
            
        