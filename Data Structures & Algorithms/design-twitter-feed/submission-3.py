from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        # Changed from list to set to prevent duplicate follows
        self.follows = defaultdict(set) 
        self.tweets = defaultdict(list)
        self.counter = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.counter))
        self.counter += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # Start with a copy of who they follow
        following_user_ids = list(self.follows[userId])
        
        # Only add themselves if they aren't already in their own follow set
        if userId not in self.follows[userId]:
            following_user_ids.append(userId)
        
        all_tweets = []
        for user_id in following_user_ids:
            all_tweets.extend(self.tweets[user_id])

        all_tweets.sort(key=lambda x: x[1], reverse=True)
        res = []

        k = min(10, len(all_tweets))
        for i in range(k):
            res.append(all_tweets[i][0])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # .add() automatically ignores duplicates
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # .discard() removes the item if it exists, and does nothing if it doesn't
        self.follows[followerId].discard(followeeId)