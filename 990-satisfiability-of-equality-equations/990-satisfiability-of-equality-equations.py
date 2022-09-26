class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        def find(a):
            if(parent[a] != a):
                parent[a] = find(parent[a])
            return parent[a]
        
        def union(a, b):
            if(find(a) == find(b)):
                return
            parent[b] = find(parent[a])
            
        
        def create_disjoint():
            for eq in equations:
                if(eq[1] == '='):
                    union(find(eq[0]), find(eq[3]))
                    
        
        parent = {c:c for c in string.ascii_lowercase}
        create_disjoint()
        print(parent)
        
        for eq in equations:
            if(eq[1] == "!" and \
              find(eq[0]) == find(eq[3])):
                return False
        
        return True
                
        