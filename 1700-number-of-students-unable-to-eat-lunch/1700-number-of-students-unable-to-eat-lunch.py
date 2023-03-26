class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stack = deque(sandwiches)
        que = deque(students)
        poped = True
        while(poped):
            poped = False
            for _ in range(len(que)):
                if(que[0] == stack[0]):
                    poped = True
                    que.popleft()
                    stack.popleft()
                    break
                
                que.append(que.popleft())
        
        return len(que)