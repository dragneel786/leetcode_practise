class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        
        def create_graph():
            g = defaultdict(list)
            for i, c in enumerate(text):
                g[c].append(i)
            
            return g
        
        
        def dfs(word, start = -1, end = -1):
            if(not word):
                ans.append([start, end])
                return 
        
            for idx in graph[word[0]]:
                if(end == -1 or end + 1 == idx):
                    dfs(word[1:], start if(start != -1) else idx, idx)
            
        
        graph = create_graph()
        ans = []
        for word in words:
            dfs(word)
        
        return sorted(ans)