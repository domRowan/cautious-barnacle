# Design Twitter

## Use cases - 5 mins

- Users can post a short message
- Users can post images/ videos
- Users can follow other users
- Users can see a timeline of posts for all the users they follow
- Users can mention other users in their posts

## Questions - 5 mins

- How many users?
  - 500 million
- How many requests per second?
  - 500 million posts per day

## Maths - 5 mins

- TPS
  - 500 million posts per day
    - 50 - 60 TPS
- Storage
  - 100 KB per image
    - 50 TB if everyone has an image
  - 10 MB per video
    - 5 PB if everyone has a video
  - 280 characters = 280 bytes
    - 150 GB for full text
- Throughput
  - Data read per second
  - Data write per second
    - Text
      - 2 MB/s
    - Image
      - 600 MB/s
    - Video
      - 60 GB/s
- Latency
  - Mention but hard to estimate
  - Add metrics

## High level design - 5 mins

- Client
- Load balancer
- Web server
- Data servers
- Database
- CDN
- Cache

## Bottlenecks - 5 mins

- Amount of traffic
- Amount of data
  - Move references to data, not data
- Reading data quickly
  - Fragment large data
- Writing data quickly
  - Fragment large data
- Decoupling
  - Media upload
    - Don't co-locate large data with metadata
  - Separate out interfaces
    - Don't deliver an entire customer object for an email address

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
- _Back end server:_
  - What actions do we need to perform
  - What data do we need to process
  - Can these be stateless
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
- _Post Storage:_
  - Metadata
    - Store this separate to the content
    - Can deliver important information about the content without delivering the whole content
    - Author -> Tweet
      - Separate table
      - Posts I uploaded
    - User -> liked OR User -> follows
      - Separate table
      - Relations
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

### Timeline service

- Get user follows list from database
- Get metadata for followed user's timelines
- Order metadata based on time
- Chunk data into sections to request
- Request first N chunks
  - Could be measured and optimized
- Add links ot media if appropriate
- Assemble timeline
- Return timeline with media links to get content from CDN

### Scale the Server

- _Horizontal Scaling:_
  - Add more hosts
    - Service should be stateless
  - Load balancer
    - Distribute load on hosts
- _Vertical Scaling:_
  - Add more CPU
  - Add more RAM
  - Add more storage
- Caching
  - See `Cache` section

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
    - Tradeoff between cpomputation and storage costs
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

### Resiliance to failure

- Segments of downloads can be retired, not just requests
  - Allows user to carry on from where they left off
  - Video
    - Segments like in Prime Video
    - Adaptive bandwidth streaming
  - Images
    - Progressive JPEG
      - Renders in scans
      - 27% decrease in p95 load times
      - 74% decrease in failure rate
