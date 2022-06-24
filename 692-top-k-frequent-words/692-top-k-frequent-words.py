class Freq:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if(self.freq != other.freq):
            return self.freq < other.freq
        else:
            return other.word < self.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = Counter(words)
        heap = []
        for w in hashmap.keys():
            heappush(heap, Freq(hashmap[w], w))
            if(len(heap) > k):
                heappop(heap)
        
        return reversed([heappop(heap).word for _ in range(len(heap))])
        
        
        