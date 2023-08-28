class MyStack:

    def __init__(self):
        self.my_stack = deque()

    def push(self, x: int) -> None:
        def reverse(a, b):
            while(a):
                b.append(a.popleft())
                
        que = deque()
        reverse(self.my_stack, que)
        self.my_stack.append(x)
        reverse(que, self.my_stack)

    def pop(self) -> int:
        return self.my_stack.popleft()
        

    def top(self) -> int:
        return self.my_stack[0]

    def empty(self) -> bool:
        return not self.my_stack


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()