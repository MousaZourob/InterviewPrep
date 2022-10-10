from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.delta = SortedDict()
        self.max = 0
        
    def book(self, start: int, end: int) -> int:
        if start not in self.delta:
            self.delta[start] = 0
        self.delta[start] += 1
        
        if end not in self.delta:
            self.delta[end] = 0
        self.delta[end] -= 1
        
        curr_sum = 0
        for d in self.delta.values():
            curr_sum += d
            self.max = max(self.max, curr_sum)
        
        return self.max

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)