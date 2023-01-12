class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        def create_tree():
            tree = defaultdict(list)
            for a, b in edges:
                tree[a].append(b)
                tree[b].append(a)
            return tree
        
        def count_labels(s = 0, p = -1):
            cnts = Counter(labels[s])
            for v in tree[s]:
                if(v != p):
                    cnts += count_labels(v, s)
            ans[s] += cnts[labels[s]]
            return cnts
        
        
        ans = [0] * n
        tree = create_tree()
        count_labels()
        return ans