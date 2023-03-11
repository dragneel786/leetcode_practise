class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        def reverse_map():
            rmap = defaultdict(str)
            for region in regions:
                main = region[0]
                for c in region[1:]:
                    rmap[c] = main
            return rmap
        
        maps = reverse_map()
        path = set([region1, region2])
        while(region1 != region2):
            region1 = maps[region1]
            region2 = maps[region2]
            if(region1 and region1 in path):
                return region1
            
            if(region2 and region2 in path):
                return region2
            
            path.add(region1)
            path.add(region2)
        
        return region1
        
        