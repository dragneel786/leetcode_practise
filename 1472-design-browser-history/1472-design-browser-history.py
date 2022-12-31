class BrowserHistory:

    def __init__(self, homepage: str):
        self.c = deque()
        self.f = deque()
        self.home = homepage

    def visit(self, url: str) -> None:
        if(self.f and self.f[-1] == url):
            self.f.pop()
        else:
            self.f.clear()
        
        self.c.append(url)

    def back(self, steps: int) -> str:
        while(self.c and steps):
            self.f.append(self.c.pop())
            steps -= 1
        
        if(self.c):
            return self.c[-1]
        return self.home

    def forward(self, steps: int) -> str:
        while(self.f and steps):
            self.c.append(self.f.pop())
            steps -= 1
        
        if(self.c):
            return self.c[-1]
        return self.home

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)