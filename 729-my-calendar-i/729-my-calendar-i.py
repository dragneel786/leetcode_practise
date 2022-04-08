class MyCalendar:

    def __init__(self):
        self.q = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_left(self.q, (start, end))
        if idx-1 >= 0 is not None and start < self.q[idx-1][1]:
            return False
        elif idx < len(self.q) and self.q[idx][0] < end:
            return False
        # add
        self.q.insert(idx, (start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)