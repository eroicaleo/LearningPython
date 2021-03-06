#!/usr/bin/env python

import collections
from heapq import heappush, heappop

TwitterInfo = collections.namedtuple('TwitterInfo', [
        'GlobalIndex',
        'TwitterID',
        'UserID',
        'Index',
    ]
)

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t_dict = collections.defaultdict(list)
        self.f_dict = collections.defaultdict(set)
        self.global_index = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if len(self.f_dict[userId]) == 0:
            self.f_dict[userId].add(userId)
        ix = len(self.t_dict[userId])
        self.t_dict[userId].append(TwitterInfo(self.global_index, tweetId, userId, ix))
        self.global_index -= 1

    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        news_feed, heap = [], []
        for u in self.f_dict[userId]:
            l = len(self.t_dict[u])
            if l > 0:
                heappush(heap, self.t_dict[u][-1])
        print(f'Inital heap: {heap}')
        while (len(news_feed) < 10) and (len(heap) > 0):
            tweet_info = heappop(heap)
            news_feed.append(tweet_info.TwitterID)
            if tweet_info.Index > 0:
                heappush(heap, self.t_dict[tweet_info.UserID][tweet_info.Index-1])
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.f_dict[followerId].add(followerId)
        self.f_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.f_dict[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

cmd = ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
arg = [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]

cmd = ["Twitter","postTweet","follow","follow","getNewsFeed","postTweet","getNewsFeed","getNewsFeed","unfollow","getNewsFeed","getNewsFeed","unfollow","getNewsFeed","getNewsFeed"]
arg = [[],[1,5],[1,2],[2,1],[2],[2,6],[1],[2],[2,1],[1],[2],[1,2],[1],[2]]

cmd = ["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","follow","getNewsFeed"]
arg = [[],[2,5],[1,3],[1,101],[2,13],[2,10],[1,2],[2,94],[2,505],[1,333],[1,22],[2],[2,1],[2]]
# expected: [null,null,null,null,null,null,null,null,null,null,null,[505,94,10,13,5],null,[22,333,505,94,2,10,13,101,3,5]]

obj = Twitter()
for i in range(1,len(arg)):
    print(f'cmd: {cmd[i]}, arg: {arg[i]}')
    print(getattr(obj, cmd[i])(*arg[i]))

# Your input: ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"][[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
# expected:[null,null,[5],null,null,[6,5],null,[5]]
