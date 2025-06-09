class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []
        
        self.following[userId].add(userId)
        
        for following in self.following[userId]:
            for tweet in self.tweets[following]:
                heappush(heap, tweet)
        
        while heap and len(feed) < 10:
            feed.append(heappop(heap)[1])
            
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
