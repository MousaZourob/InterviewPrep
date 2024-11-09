class RandomizedCollection:

    def __init__(self):
        self.data = []
        self.indexes = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.indexes[val].add(len(self.data))
        self.data.append(val)
        return len(self.indexes[val]) == 1
        
    def remove(self, val: int) -> bool:
        if not self.indexes[val]:
            return False

        removed_index = self.indexes[val].pop()
        last_element = self.data[-1]
        
        self.data[removed_index] = last_element
        self.indexes[last_element].add(removed_index)
        self.indexes[last_element].remove(len(self.data) - 1)
        
        self.data.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()