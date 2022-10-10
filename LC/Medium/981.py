from sortedcontainers import SortedDict

class TimeMap:
    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.data:
            self.data[key] = SortedDict()
        
        self.data[key][timestamp] = value
            
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.data:
            return ""
        
        it = self.data[key].bisect_right(timestamp)
        if it == 0:
            return ""
        
        return self.data[key].peekitem(it - 1)[1]
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)