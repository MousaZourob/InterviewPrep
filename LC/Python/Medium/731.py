from sortedcontainers import SortedDict

class MyCalendarTwo:
    def __init__(self):
        self.delta = SortedDict()

    def book(self, start: int, end: int) -> bool:
        if start not in self.delta:
                self.delta[start] = 0
        self.delta[start] += 1
        
        if end not in self.delta:
                self.delta[end] = 0
        self.delta[end] -= 1
        
        curr_sum = 0
        for d in self.delta.values():
            curr_sum += d
            
            if curr_sum >= 3:
                self.delta[start] -= 1
                self.delta[end] += 1
                return False
        
        return True
            


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)