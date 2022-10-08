class TimeMap:
    def __init__(self):
        self.data = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key][timestamp] = value
            
    def get(self, key: str, timestamp: int) -> str:
        if not self.data[key]:
            return ""
        
        for curr_time in range(timestamp, 0, -1):
            if curr_time in self.data[key]:
                return self.data[key][curr_time]
        
        return ""
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)