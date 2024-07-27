class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        def floyd():
            g = [([inf] * 26) for _ in range(26)]
            for i in range(26):
                g[i][i] = 0
                
            for i in range(len(original)):
                o_idx = ord(original[i]) - 97
                c_idx = ord(changed[i]) - 97
                g[o_idx][c_idx] = min(g[o_idx][c_idx], cost[i])
            
            for k in range(26):
                for i in range(26):
                    for j in range(26):
                        g[i][j] = min(g[i][j], g[i][k] + g[k][j])
        
            return g
                
        graph = floyd()
        # print(graph)
        cost = 0
        for src, tar in zip(source, target):
            # print(src, tar, graph[ord(src) - 97][ord(tar) - 97])
            if graph[ord(src) - 97][ord(tar) - 97] == inf:
                return -1
            
            cost += graph[ord(src) - 97][ord(tar) - 97]
        
        return cost
            