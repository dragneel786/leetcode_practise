class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        for ide, score in items:
            heappush(scores[ide], score)
            if(len(scores[ide]) > 5):
                heappop(scores[ide])
        
        res = []
        for ide, sc in scores.items():
            res.append([ide, sum(sc) // 5])
        
        return sorted(res, key=lambda x: x[0])