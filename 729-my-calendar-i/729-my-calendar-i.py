class MyCalendar:

    def __init__(self):
        self.books = []
    
    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_left(self.books, (start, end))
        if(idx - 1 >= 0 and self.books[idx - 1][1] > start):
            return False
        if(idx < len(self.books) and self.books[idx][0] < end):
            return False
        
        self.books.insert(idx, (start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)