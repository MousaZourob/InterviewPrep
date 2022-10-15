from sortedcontainers import SortedList

class MaxStack:

    def __init__(self):
        self.stack = SortedList()
        self.sorted = SortedList()
        self.index = 0

    def push(self, x: int) -> None:
        self.stack.add((self.index, x))
        self.sorted.add((x, self.index))
        self.index += 1

    def pop(self) -> int:
        idx, num = self.stack.pop()
        self.sorted.remove((num, idx))
        return num

    def top(self) -> int:
        return self.stack[-1][1]

    def peekMax(self) -> int:
        return self.sorted[-1][0]

    def popMax(self) -> int:
        num, idx = self.sorted.pop()
        self.stack.remove((idx, num))
        return num


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()