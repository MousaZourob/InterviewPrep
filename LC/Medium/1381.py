class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return
        
        self.stack.append([x, 0])

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        num, inc = self.stack.pop()
        
        if len(self.stack) > 0:
            self.stack[-1][1] += inc
        return num + inc
        
    def increment(self, k: int, val: int) -> None:
        if len(self.stack) == 0:
            return
        if len(self.stack) >= k:
            self.stack[k-1][1] += val
        else:
            self.stack[-1][1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)