## Understand the requirements

Clarify the system's constraints

Clarify what the inputs and expected outputs are

Identify what use cases the system needs to satisfy

Ask for confirmation on ideas before continuing

Show your thought process behind your choices

Understand design tradeoffs - everything is a tradeoff

Pragmatic approach to solving the problem

Sketch out the important components

Sketch out the connections between the components

Sketch out key data structures

Sketch out key algorithms

Discuss tech stack

- programming language
- libraries
- OS and hardware
- Services

Discuss tradeoffs at every step

Discuss the implementation time

Discuss number of requests

Discuss reads vs writes percentages

Discuss amount of data written/ read per second

Discuss total storage required over 5 years

Discuss extensibility

Discuss scalability

Discuss caching

Discuss testability

Discuss security

Discuss bottlenecks

Discuss internationalization/ globalization

Discuss code reuse

Separate data from metadata

Clarify service level agreements (SLAs)

Clarify performance of the system

Discuss metrics

## Concurrency

Threads
Deadlocks
Starvation
Consistency
Coherence

How to parallelize the algorithm

## Decomposition

Split out the functionality, architecture and code into managable reusable components.

Could decompose based into categories absed on the stake holders in the system

Could decompose the architecture into front end and back end functionality

- Front end concerns
- view management
- input management
- reporting functionality

- Back end sections
- middleware
- storage
- database
- cron services
- algorithms

## Availability and reliability

What parts of the system can fail

- what happens if a host fails
- what happens if a DB node fails
- what happens if a network call times out
  How does this change if the system is distributed

How to cope with network failures

- retry mechanism
- exponential backoff

## Sharding data

- order of appearance
- hash values
- arbritrary
- frequency of use

## Time of operation

- 1 nano seconds from cache
- 100 nano seconds from memory

- Send 2K bytes over 1 Gbps network 20 micro seconds
- Read 1MB sequentially from memory 250 micro seconds
  - 10X slower
- Roundtrip within same datacenter 500 micro seconds
  - 2X slower
- Read 1MB sequentially from disk 20 milli seconds
  - 40X slower
- Send packet CA -> Netherlands -> CA 150 milli seconds
  - 7X slower

## Usage numbers

- Facebook users
  - 1 billion
- Twitter users
  - 500 million
- Posts per day
  - 500 million

## Networking

Inter process communication

TCP/IP

Throughput
Latency

## Abstraction

Understand the system you are building on

how the OS works - ish

- Caching in the OS

how the database works

Docker
VMs

## Parallelism

Split the problem into sub problems which can be solved independently on different machines.

Useful when dealing with scale

- if the problem is too large to fit into a single machine
- would take a long time if processed on a single machine

Decompose the problem into sub problems

Each sub problem should be solvable independently

The solution to the orignial problem should be easily recreated from the solutions to the sub problems

Measure the eficciency in terms of

- CPU
- RAM
- Network Bandwidth
- number of database or memory addresses

## Caching

Compute something, store it and look it up at a later date

Great whenever computations are repeated

Great when a system is responding to the same request multiple times

Complications include updating the cache in the presence of many requests

- can use a second cache and hot swap
- if using a second cache then warm this up before swapping this in
- duplicate production requests and send these to the backup before hot swapping

Think about how caching interacts with multithreading

## Databases

SQL - relational database

- MySQL, Oracle
- table based
- represent data as a a series of rows - excel
- Not the best fit for heirarchical data
- use a strict data schema
- better for structured data
- Vertically scalable
- Scaled by improving the hardware on which the DB is running
- Increase CPU, RAM, HDD -> SSD
- Accessed using structured query language (SQL)
- Good for complex queries
- Good for transactional actions
- guaranteed atomicity of data
- guaranteed integrity of data
- Values should follow ACID properties
- Atomicity
- Consistency
- Isolation
- Durability
- MySQL
  - Replication can provide some scalability
  - Sharding can support large number of write operations
  - Divide into multiple chunks using low cost servers so this can be cost effective
  - Memcache
  - Open source, free

No SQL - non related - distributed

- Mongo, Redis
- document based
- key value pairs
- graph databases
- Good for heirarchical data
- do not have a standard schema to be adhered to
- dynamic schema allows for unstructured data
- horizontally scalable
- scaled by increasing the number of hosts in the database fleet
- Easier to scale this way to handle increase in traffic
- Access based on the collection of documents by key
- Access language changes from database to database
- Not so good for complex queries
- preferred for large data sets (big data)
- Not stable enough for high load complex transctions
- Values should follow CAP theorem
- Consistency
- Availability
- Partition tolerance
- MongoDB
  - stores informatin in JSON like documents
  - good performance for simple queries
  - All related data is in same document so no need for join calls
  - Horizontally scalable by adding hosts to the fleet
  - can be sharded
  - Can modify schema without modifying existing data
- Redis
  - can store keys as hashes, lists, strings, unsorted sets
  - can implement redis as a cache by adding keys with a TTL
  - Very fast

## Searching

- Look into Elastic search
- Stemming
- Reducing a word down to increase the number of matches you get
- How this interacts with databases

## Load balancing

consistant hashing

- algo

## Accessibility

- How can people use your system

## Portability

- Does the solution easily move from web to mobile

## Async vs sync

- Don't block the customer
- Can use queues to perform tasks

## Storing/ Moving data

- Don't move large items around, move references
- Simple upload to S3 for large files first then can process/ change
- Cache things which are accessed often
- Move things to cold storage which are not accessed often - saves money
