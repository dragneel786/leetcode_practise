class Tweets:
    def __init__(self, id = -1, timestamp = -1, next = None):
        self.id = id
        self.timestamp = timestamp
        self.next = next
    
    def __lt__(self, other):
        return other.timestamp < self.timestamp
        
class Users:
    def __init__(self, userId = -1, head = None):
        self.id = userId
        self.head = head

class Twitter:

    def __init__(self):
        self.ff = defaultdict(set)
        self.mr = defaultdict(lambda:0)
        self.ts = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = Tweets(tweetId, self.ts)
        if(not self.mr[userId]):
            self.mr[userId] = Users(userId, tweet)
        else:
            tweet.next = self.mr[userId].head
            self.mr[userId].head = tweet
        self.ts += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        follows = [self.mr[userId].head] if(self.mr[userId]) else []
        for f in self.ff[userId]:
            if(self.mr[f]):
                follows.append(self.mr[f].head)
        heapify(follows)
        res = []
        j = 10
        while(follows and j):
            t = heappop(follows)
            res.append(t.id)
            t = t.next
            if(t):
                heappush(follows, t)
            j -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.ff[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if(followerId in self.ff and followeeId in self.ff[followerId]):
            self.ff[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)