class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        popped = True
        students = deque(students)
        sandwiches = deque(sandwiches)
        while(popped):
            popped = False
            for _ in range(len(students)):
                if students[0] == sandwiches[0]:
                    students.popleft()
                    sandwiches.popleft()
                    popped = True
                    break
                
                students.append(students.popleft())
            
        return len(students)
                
        