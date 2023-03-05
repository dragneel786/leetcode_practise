class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        rcounts = Counter(ranks)
        scounts = Counter(suits)
        if(len(scounts) == 1):
            return "Flush"
        
        count_values = set(rcounts.values())
        if(set([3,4,5]) & count_values):
            return "Three of a Kind"
        
        if(2 in count_values):
            return "Pair"
        
        return "High Card"