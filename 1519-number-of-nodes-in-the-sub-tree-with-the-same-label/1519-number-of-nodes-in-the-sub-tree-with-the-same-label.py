class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        def create_tree():
            tree = defaultdict(list)
            for a, b in edges:
                tree[a].append(b)
                tree[b].append(a)
            
            return tree
        
        def count_labels(s = 0, visited = set()):
            visited.add(s)
            lcount = Counter()
            for v in tree[s]:
                if(v not in visited):
                    lcount.update(count_labels(v, visited))
            
            lcount[labels[s]] += 1
            ans[s] += lcount[labels[s]]
            visited.remove(s)
            return lcount
        
        
        ans = [0] * n
        tree = create_tree()
        count_labels()
        return ans