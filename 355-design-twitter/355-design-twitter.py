class Twitter:

    def __init__(self):
        self.ff = defaultdict(set)
        self.mr = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.mr.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        follows = self.ff[userId]
        res = []
        for m in range(len(self.mr) - 1, -1, -1):
            u, t = self.mr[m]
            if(u in follows or u == userId):
                res.append(t)
                
            if(len(res) == 10):
                break
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