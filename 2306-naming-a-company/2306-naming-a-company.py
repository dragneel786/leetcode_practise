class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        
        def create_map():
            first = defaultdict(set)
            for idea in ideas:
                first[idea[0]].add(idea[1:])
            return first

        fmap = create_map()
        count = 0
        keys = list(fmap.keys())
        for i, k1 in enumerate(keys):
            for k2 in keys[i + 1:]:
                mutual_count = len(fmap[k1] & fmap[k2])
                count += 2 * ((len(fmap[k1]) - mutual_count) * 
                              (len(fmap[k2]) - mutual_count))


        return count

                
                
                
                
        