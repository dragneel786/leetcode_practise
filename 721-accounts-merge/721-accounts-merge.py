class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Create email-> (n, e1), (n, e2) pairs
        # then for each email, traverse all it's pairs and mark visited.
        # Keep appending the email to an array.
        
        def createGraph():
            g = defaultdict(list)
            for acc in accounts:
                for c in combinations(acc[1:], 2):
                    g[c[0]].append(c[1])
                    g[c[1]].append(c[0])
            return g
                    
        def dfs(e):
            seen.add(e)
            temp = [e]
            for acs in graph[e]:
                if(acs not in seen):
                    temp.extend(dfs(acs))
            return temp
            
        
        graph = createGraph()
        seen = set()
        res = []
        for acc in accounts:
            if(acc[1] not in seen):
                ans = [acc[0]]
                ans.extend(sorted(dfs(acc[1])))
                res.append(ans)
        return res
        
        
            
            