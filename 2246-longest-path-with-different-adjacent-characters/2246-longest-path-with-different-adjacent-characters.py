class Solution:
    def longestPath(self, parent: List[int], label: str) -> int:
        
        def create_tree():
            tree = defaultdict(list)
            for i, p in enumerate(parent):
                tree[p].append(i)
            return tree
        
        
        def find_large(paths, s, p):
            nonlocal max_path
            first = second = 0
            for pa in paths:
                if(pa > first):
                    second = first
                    first = pa
                
                elif(pa > second):
                    second = pa
            
            max_path = max(max_path, first + second + 1)
            return (first + 1) if(label[s] != label[p]) else 0
            
    
        def long_path(s = 0, p = -1):
            paths = []
            for v in tree[s]:
                paths.append(long_path(v, s))
            return find_large(paths, s, p)
    
        tree = create_tree()
        max_path = 0
        long_path()
        return max_path
        