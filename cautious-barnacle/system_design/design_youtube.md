# Design YouTube

## Use cases

- Deliver video to millions of users
- Videos should load as fast as possible
- Users can upload videos
- Users can like and share videos

## Overview

- _Storage:_
  - What database do you use?
  - How do you design the database schema?
  - How do you store large data (videos and images)?
- _Scalability:_
  - How do you scale the whole system?
  - How do you scale the storage?
- _Web Server:_
  - How do front end clients (web mobile) get data?
  - What happens if a web server fails?
  - Who handles authentication?
  - Who handles user data?
  - Who handles metrics?
- _Cache:_
  - Do you need to cache in layers?
    - How do you cache user data?
    - How do you cache large data (videos and images)?
  - How do you keep the cache relevant?
  - What happens if a cache fails?
- _Security:_
  - How to detect malicious users

### Storage and data model

- _Relational database:_
  - MySQL
  - This is what youtube actually uses
- _User Model:_
  - Auth data
    - Separate table for limiting access
  - General data
    - Email address
    - Name
- _Video Storage:_
  - Metadata
    - Store this separate to the video
    - Can deliver important information about the video without delivering the whole video
    - Author -> Video
      - Separate table
      - Videos I uploaded
    - User -> Watched OR User -> Liked
      - Separate table
      - Customers also watched
      - People also liked
  - Video content
    - Stored separately, easier to manage at scale
    - Dedicated storage, better performance
    - Content delivery network (CDN)
      - Serve content with high availability and high performance
      - Nodes close to customer
      - Store popular content
        - Good for localization
      - Long tail items
        - Separate strategy
        - Colder storage for cost efficiency

### Scale the database

- _Premature Optimization:_
  - Unlikely to need partition from day 1
  - Scale when you need it
- _Identify The Bottleneck:_
  - Serve videos faster than other features
  - Prioritise metadata over other features
- _Single Server:_
  - Simple place to begin
- _Master/ Slave Model:_
  - Depends on situation
  - Single master, multiple read nodes
  - Single master, multiple write nodes
- _Partitioning/ Sharding:_
  - Split by user location
  - Split by order of apperance (when a request was processed)
  - Split by hash values of a key
  - Split by frequency of use
  - Split randomly

### Cache

- _LRU Cache:_
  - Lookup
    - If item is in cache
      - Return it
      - Set last used datetime
    - If not in cache and space available
      - Get it
      - Return it
      - Add to cache
      - Set last used datetime
    - If not in cache and no space
      - Get it
      - Return it
      - Evict the least recently used item from cache
      - Add to cache
      - Set last used datetime
- _Eviction:_
  - LRU
    - As above
  - Random Replacement
    - does what is says on the tin
  - W-TinyLFU
    - Calculate frequency of usage within a time window
    - Best for expiring items which are no longer popular
- _Concurrency:_
  - Two requests competing for the last empty slot in the cache
    - Last item wins
  - Using a lock
    - Bad performance
  - Sharding
    - Same problem in multiple places
  - Commit logs
    - Store all the transactions into logs
    - Use BG process to parse the logs and update cache
    - Used in databases
- _Distributed Cache:_
  - Cache on multiple machines for scale
  - Hash table to map a resource to a machine
- Expiration policy
  - How to handle expiring specific items from the cache
  - Time to live (TTL)
    - Remove an item after a certain time
  - Forced expiry
    - Security flaw/ update

### Security

- View hacking
  - Check the IP address a request is coming from
    - Block requests if too frequent
  - Check previous interactions from IP address
    - If suspicious, then block it
  - Check interaciton data
    - Compare with prediction patterns of real data
    - View count
    - View time
    - Comment count
    - Share count

### Web server

- Youtube webserver originally built in python
  - Rapid flexible development and deployment
  - Fast to iterate
- Python performance issues
  - C extensions to optimize critical sections
- Multiple web servers accesed from a load balancer
- As little logic as possible in web werver
  - Fetch information from downstream services
