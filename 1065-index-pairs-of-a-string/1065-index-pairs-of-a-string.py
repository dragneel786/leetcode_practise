class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        
        def create_graph():
            g = defaultdict(list)
            for i, c in enumerate(text):
                g[c].append(i)
            
            return g
        
        
        def dfs(i, end = -1):
            nonlocal word
            if(i == len(word)):
                ans.append([end - len(word) + 1, end])
                return 
        
            for idx in graph[word[i]]:
                if(end == -1 or end + 1 == idx):
                    dfs(i + 1, idx)
            
        
        graph = create_graph()
        ans = []
        for word in words:
            dfs(0)
        
        return sorted(ans)