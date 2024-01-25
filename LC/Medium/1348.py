class TweetCounts:

    def __init__(self):
        self.records = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.records[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        frequency = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400 
        chunks = (endTime - startTime) // frequency + 1
        ans = []
        curr_time = startTime
        
        while curr_time <= endTime:
            next_time = min(curr_time + frequency, endTime + 1)
            ans.append(bisect_left(self.records[tweetName], next_time) - bisect_left(self.records[tweetName], curr_time))
            curr_time += frequency
        
        return ans

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)