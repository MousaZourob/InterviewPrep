class HitCounter:

    def __init__(self):
        self.cache = [[0,i+1] for i in range(300)]
        
    def hit(self, timestamp: int) -> None:
        idx = (timestamp - 1)%300
        if self.cache[idx][1] == timestamp:
            self.cache[idx][0] += 1
        else:
            self.cache[idx][0] = 1            
            self.cache[idx][1] = timestamp   

    def getHits(self, timestamp: int) -> int:
        cnt = 0
        for x in self.cache:
            c,t = x[0],x[1]
            if c > 0 and timestamp - t < 300:
                cnt += c
        return cnt


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)