class RandomizedSet:

    def __init__(self):
        self.data = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.data)
        self.data.append(val)
        
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        
        index = self.dict[val]
        last_element = self.data[-1]
        
        self.data[index] = last_element
        self.dict[last_element] = index
        
        self.data.pop()
        del(self.dict[val])
        
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()