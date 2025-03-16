class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        color_map = dict()
        tot_adj, res = 0, []
        for idx, color in queries:
            if idx in color_map:
                tot_adj -= color_map.get(idx - 1, -1) == color_map[idx]
                tot_adj -= color_map.get(idx + 1, -1) == color_map[idx]
            
            color_map[idx] = color
            tot_adj += color_map.get(idx - 1, -1) == color_map[idx]
            tot_adj += color_map.get(idx + 1, -1) == color_map[idx]
            res.append(tot_adj)

        return res
