class Solution:
    def longestPath(self, parent: List[int], label: str) -> int:
        
        def create_tree():
            tree = defaultdict(list)
            for i, p in enumerate(parent):
                tree[p].append(i)
            return tree
        
    
        def long_path(s = 0, p = -1):
            nonlocal max_path
            first = second = 0
            for v in tree[s]:
                val = long_path(v, s)
                if(val > first):
                    first, second = val, first
                
                elif(val > second):
                    second = val
            
            max_path = max(max_path, first + second + 1)
            
            if(p != -1 and label[s] == label[p]):
                return 0
            
            return first + 1

        tree = create_tree()
        max_path = 0
        long_path()
        return max_path
        