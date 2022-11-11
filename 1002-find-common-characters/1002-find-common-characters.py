class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = reduce(lambda a, b: Counter(a) & Counter(b), words)
        return [ch for ch, co in counter.items() for _ in range(co)]
        
            
            
            