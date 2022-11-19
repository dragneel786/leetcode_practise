class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        for ide, score in items:
            heappush(scores[ide], score)
        
        res = []
        for ide, sc in scores.items():
            res.append([ide, sum(nlargest(5, sc)) // 5])
        
        return sorted(res, key=lambda x: x[0])