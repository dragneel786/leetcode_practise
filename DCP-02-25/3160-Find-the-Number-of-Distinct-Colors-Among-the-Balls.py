class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]: 
        res = []
        color_map = dict()
        color_counts = Counter()
        for val, color in queries:
            p_color = color_map.get(val, -1)
            color_map[val] = color

            if p_color != -1:
                color_counts[p_color] -= 1
                if color_counts[p_color] == 0:
                    del color_counts[p_color]

            color_counts[color] += 1
            res.append(len(color_counts))
        
        return res



