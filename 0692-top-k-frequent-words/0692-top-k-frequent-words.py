class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        class Node:
            def __init__(self, word = "", count = 0):
                self.word = word
                self.count = count
            
            def __lt__(self, other):
                return self.count < other.count or\
            (self.count == other.count and\
            self.word > other.word)
                
            
        heap = []
        for w, c in Counter(words).items():
            new_node = Node(w, c)
            heappush(heap, new_node)
                
            if(len(heap) > k):
                heappop(heap)
        
        return [heappop(heap).word for _ in range(len(heap))][::-1]
                

        