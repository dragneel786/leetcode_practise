class MyCalendarTwo:

    def __init__(self):
        self.single = []
        self.double = []
        

    def book(self, start: int, end: int) -> bool:
        s, d = self.single, self.double
        for i,j in d:
            if(start < j and end > i):
                return False
        
        for i,j in s:
            if(start < j and end > i):
                d.append([max(start, i), min(j, end)])
        s.append([start, end])
        return True
        
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)