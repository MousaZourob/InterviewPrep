class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.freq[val] += 1

        if self.freq[val] > len(self.stack):
            self.stack.append([val])
        else:
            self.stack[self.freq[val] - 1].append(val)

    def pop(self) -> int:
        res = self.stack[-1].pop()

        if len(self.stack[-1]) == 0:
            self.stack.pop()
        
        self.freq[res] -= 1

        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()