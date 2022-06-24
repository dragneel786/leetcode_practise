class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = Counter(words)
        return nsmallest(k, hashmap.keys(), key=lambda x: [-hashmap[x], x])
        
        
        