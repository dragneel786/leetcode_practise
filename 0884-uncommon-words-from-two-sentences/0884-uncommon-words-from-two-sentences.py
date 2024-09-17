class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ws1 = Counter(s1.split())
        ws2 = Counter(s2.split())
        # print((ws1 - ws2), (ws2 - ws1))
        return [k for k, v in (ws1 + ws2).items() if v == 1]
            
            
            
        
        