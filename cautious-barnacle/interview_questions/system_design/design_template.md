# Design <SOMETHING>

## Use cases/ Key performance indicators (KPIs)- 5 mins

- Customers can ...

### Questions for Use Cases

- Why is this system required?
- Who is going to use the system?
- What is the key feature of the system?
  - How does the system perform this task?
- How do the customers interact with the system?
- When is the system used?
- Where...
  - Is the system located?
  - Are the customers located?

* How many users?
  - Add metrics for
    - Sign ups
    - Daily active users
* How many requests per second?
  - Add metrics for
    - Engagement
    - Host metrics (CPU, memory...)
    - Traffic pattern predictions
* How fast does the system have to be?
  - Add metrics for
    - Latency
* What is the expected availability?
  - Add metrics for
    - Failure rate
    - Retry rate
* Global system or regional?
  - Language concerns
  - Latency concerns

## Maths - 5 mins

- TPS
- Storage
- Throughput
  - Data read per second
  - Data write per second
- Latency
  - Mention but hard to estimate
  - Add metrics

## High level design - 5 mins

- Client
- Load balancer
- Web server
- Data servers
- Storage interface
- Storage/ Database access layer
- Database/ in memory storage, disk storage
- CDN
- Cache
- Key data structures
- Key algorithms

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
- Implementation time
  - If time to market is important this might affect some of your decisions

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

- Interaction hacking
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

- Multiple web servers accesed from a load balancer
- As little logic as possible in web server
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

### Debugging

- Tracing in a distributes system is difficult
  - Metrics should show health at each point
  - Every interaction shares a common ID for tracing
- Fan out of service calls makes things slow quickly
  - If every service has 1% slow calls and you call 100 services, likely you will get a slow response from one of them

### Testing

- Load testing
  - Test the performance of KPIs against 2X max traffic
- Chaos/ Failure testing
  - See what happens when you
    - Take out a server
    - Take out an availability zone
    - Fail over to a back up
    - Remove stored content
