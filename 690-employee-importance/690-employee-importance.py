"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = dict()
        for emp in employees:
            graph[emp.id] = emp
        
        q = deque([id])
        seen = set([id])
        total_importance = 0
        while(q):
            for _ in range(len(q)):
                emp = graph[q.popleft()]
                total_importance += emp.importance
                for sub in emp.subordinates:
                    if(sub not in seen):
                        q.append(sub)
                        seen.add(sub)
        return total_importance
                    
                
            