# 1. Course Schedule II

Time - O(N)    -->  Never does more than the amount of prerequesites 
Space - O(N)   -->  recursive stack space 

Approach:
- Exact same as course schedule 1, but build an array as we backtrack

- We use DSF, searching through course dependancies, until we hit a course with no dependancies or dependancies we've taken

- add them into the result array as we backtrack, the base case (class with no dependancies) will get added first
    - leading to classes only being added their dependancies are in the result array
- Mark all courses in that path as taken

- cycle detection: we simply record the depth as we recursively search for a class with satisfiable dependancies
    - if that depth goes over the amount of classes possible, we've already searched through all possible classes

# _______________________________________________________________________________________________________________________________________

# 2. Divide Two Integers

Time - O(log(y/x))   - We're multipying divisor by 2 multiple times, instead of just looping y - x and seeing how many times it takes
Space - O(1)

Approach:
- Idea: The brute force approach would just be doing a loop, and seeing how many times you can subtract x from y
- A way to make this faster, is to use bit manipulation to left shift divisor as many times as we can, unless it'd be bigger than divisor
        - left shifting ( << ) is equivilent to multiplying a number by 2
- so if the divisor can left shift 4 times, it means you can atleast fit it inside the dividend 16 times (1 >> 4) = 16
- set dividend as remainder, then reset the divisor back to original value
    
- example: divisor: 3, dividend: 60
    - 3 << 4 = 48
    - 1 << 4 = 16 (multiplier)
    - So 3 fits into 60 atleast 4 times
    - repeat with the remainer: 12
    - 3 << 3 = 12
    - 1 << 3 = 4 (multiplier) 

    quotient = 16 + 4 = 20

# _______________________________________________________________________________________________________________________________________

# 3. coin_change

TIme - O(N * amount)  --> for each amount possible, we'll at most try each coin on it
Space - O(amount)

Approach:
- We use backtracking to try every single combination of coins.
- we try every coin on each amount, saving the best into our cache

Code:
- to implement combinations, we use a for loop with a recursive approach
- we save the best from the for loop, adding it to our cache after
- we use an array where index = amount. Array is faster than a hashmap, but might use unneeded space

# _______________________________________________________________________________________________________________________________________

# 4. Twitter Design

Functional Requirements:
  1. Users can post tweets
  2. Users can reply to tweets (using a threaded conversation)
  3. users can follow/unfollow others
  4. users can view news feed of other posts from people they follow
  5. users can like/favorite tweets
  6. users can tag others in tweets
  7. users can send direct messages to other users
  8. trending posts/tweets should be displayed to the users
  9. tweets can be private / public

Non-Functional Requirements
  1. System should be eventually consistant (follower count delay is okay)
  2. System should support high 
  3. low latency feed generation
  4. scale to billions of users and millions of quaries / second
  5. ensure reliablity and durability of tweets and user actions

Extended Requirements
  1. support hashtags and search for them
  2. support media attachment (video / photos)
  3. push notifications for likes, follows, mentions
  4. block / mute / report functionality 

Assumptions
  2 B monthly users
  100 M daily users
  10 tweets avg / user / day
  200 bytes avg / tweet

Storage Estimation
  10 tweets / user / day  --> 1 B tweets a day
  1 B * 200 bytes  --> 200 GB / day
  200 GB * 365 --> 73 TB per year 

Bandwith Estimation
  1 B * 200 B --> 200 GB / day
  200 GB / 86400 = 2.31 MB / SEC
  
High Level Design
  tweet service -- store all tweets
  user graph service -- handles follows, unfollows
  DM service -- handles direct messaging
  trending service -- identifies popular hashtags and posts
  search service -- search mentions and hashtags
  notification service -- support push notifications

  Feed Generator Service -- build users feed
      -- users with low followers can be sent posts right away
      -- users with millions of followers can be sent posts dynamically over time once they've opened the app

  DB for tweets -- non-relational database (since sync isn't super important, we'd rather take the better scaling)
  DB for DM's   -- relational database (DM's are more important for real time)
  Distributed cache -- track frequently accessed tweets and DM's
  Load Balancer -- route user request to correct service, use load balancing model to increase performance 

End-to-End flow
  Goal: User A posts a tweet
    1. clients sends tweet to LB
    2. LB routes to tweet service
    3. tweet service validates and stores in tweet DB
    4. tweetID is sent to feed Generator
    5. feed generator pushes to all followers queues (lazy push for accounts with millions of followers)
    6. feed queue stored in Redis 

  Goal: User B fetches news tweet
    1. clients sends request to FeedService
    2. feed services reads from either precomputed feed in redis or queries followers + recent tweets (if high followers)
    3. returns list of tweets with metadata, eg likes, replies

  Goal: User B likes tweet
    1. client sends action to tweet service
    2. tweet service logs it, updates tweet storage, might trigger push notification service

API Design
  Client:
    send_message(fromUser, convId, enc_message)
    pull_messages(fromUser, convId) -> enc_message[]
    recv_messages(fromUser, convId, enc_message[])
    mark_read(convId, timestamp) — mark all messages before timestamp as read

    get_feed(userId, cursor?) -> tweet[] → Returns a list of tweets in feed, optionally paginated via cursor
    like_tweet(userId, tweetId)
    retweet(userId, tweetId)
    search(query) -> tweet[] → Search hashtags, mentions, keywords

  Server:
    recv_message(fromUser, convId, enc_message) — receive from client
    store_message(fromUser, convId, enc_message) — persist to DB
    get_messages(convId, fromTimestamp) -> enc_message[] — lazy load old messages
    mark_read(convId, user, timestamp)

    generate_feed(userId) -> tweet[]
    Either lazy (on request) or eager (on write)
    store_tweet(tweet)
    update_trending(tweet)
    index_tweet(tweet) — for search service

Data Partitioning
  User-related data → hash(userId) mod N
  Tweet storage → time-based sharding or user-based
  Follow graph → partition by userID