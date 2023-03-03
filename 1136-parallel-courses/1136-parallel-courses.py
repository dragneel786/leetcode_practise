class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        def course_graph():
            course = defaultdict(list)
            pcount = [0] * (n + 1)
            for a, b in relations:
                course[a].append(b)
                pcount[b] += 1
        
            return course, pcount
        
        course_map, pre_count = course_graph()
        q = deque()
        for cn in range(1, n + 1):
            if(not pre_count[cn]):
                q.append(cn)
        
        taken = 0
        sem = 0
        while(q):
            for _ in range(len(q)):
                course = q.popleft()
                for p in course_map[course]:
                    pre_count[p] -= 1

                    if(not pre_count[p]):
                        q.append(p)

                taken += 1
            
            sem += 1
        
        return sem if(taken == n) else -1
            
                
        
        
                
        