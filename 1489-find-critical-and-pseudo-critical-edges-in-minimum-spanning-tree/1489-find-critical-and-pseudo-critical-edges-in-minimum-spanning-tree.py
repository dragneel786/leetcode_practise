class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        class Disjoint:
            def __init__(self, n):
                self.parent = {a:a for a in range(n)}
            
            def union(self, a, b):
                pa, pb = self.find(a), self.find(b)
                if(pa != pb):
                    self.parent[pb] = pa
                    return False
                return True

            def find(self, a):
                if(self.parent[a] != a):
                    self.parent[a] = self.find(self.parent[a])
                return self.parent[a]

            def verify(self):
                count = 0
                for a in range(n):
                    if a == self.parent[a]:
                        count += 1

                return count == 1
                
               
        def kruk(include, exclude):
            uset = Disjoint(n)
            cost = 0
            if(include != -1):
                e, _, v1, v2 = values[include]
                uset.union(v1, v2)
                cost += e
            
            for j in range(len(values)):
                e, _, v1, v2 = values[j]
                if(j == include or j == exclude\
                   or uset.union(v1, v2)):
                    continue
                    
                cost += e
                
            
            return cost if uset.verify() else inf

        values = [(e,i,a,b) for i, (a, b, e) in enumerate(edges)]
        values.sort()
        min_weight = inf
        fixed, non_fixed = [], []
        
        for i in range(-1, len(values)):
            if(i == -1):
                min_weight = kruk(-1, -1)
                continue
            
            _, k, _, _ = values[i]
            exc = kruk(-1, i)
            if(exc > min_weight):
                fixed.append(k)
            else:
                inc = kruk(i, -1)
                if(inc == min_weight):
                    non_fixed.append(k)
        
        return [fixed, non_fixed]
        