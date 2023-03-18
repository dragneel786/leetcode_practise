class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = deque()
        self.fwd = deque()
        self.hpage = homepage

    def visit(self, url: str) -> None:
        self.curr.append(url)
        self.fwd.clear()

    def back(self, steps: int) -> str:
        while(self.curr and steps):
            steps -= 1
            self.fwd.append(self.curr.pop())
        
        return self.curr[-1] if(self.curr) else self.hpage

    def forward(self, steps: int) -> str:
        while(self.fwd and steps):
            steps -= 1
            self.curr.append(self.fwd.pop())
        
        return self.curr[-1] if(self.curr) else self.hpage


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)