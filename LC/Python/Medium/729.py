from sortedcontainers import SortedList

class MyCalendar:
    def __init__(self):
        self.data = SortedList()

    def book(self, start: int, end: int) -> bool:
        it = self.data.bisect_right([start, end])
        
        if (it > 0 and self.data[it - 1][1] > start) or (it < len(self.data) and self.data[it][0] < end):
            return False
        
        self.data.add([start,end])
        
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)