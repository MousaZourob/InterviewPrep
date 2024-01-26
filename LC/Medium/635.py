class LogSystem:

    def __init__(self):
        self.logs = {}
        
    def put(self, id: int, timestamp: str) -> None:
        self.logs[id] = timestamp

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        index = {'Year': 5, 'Month': 8, 'Day': 11, 'Hour': 14, 'Minute': 17, 'Second': 20}[granularity]
        ans = []
        
        start_time = start[:index]
        end_time = end[:index]
        
        for id, timestamp in self.logs.items():
            if start_time <= timestamp[:index] <= end_time:
                ans.append(id)
        
        return ans

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)