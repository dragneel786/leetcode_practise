class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        idx_map = defaultdict(list)
        for i, companies in enumerate(favoriteCompanies):
            for company in companies:
                idx_map[company].append(i)
        
        res = set()
        for i, companies in enumerate(favoriteCompanies):
            counts = Counter()
            res.add(i)
            n = len(companies)
            for company in companies:
                for idx in idx_map[company]:
                    counts[idx] += 1
                    if(counts[idx] == n and idx != i):
                        res.discard(i)
            
        return res
                        
            
            
        