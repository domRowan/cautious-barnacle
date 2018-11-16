'''
Understand the requirements

Understand design tradeoffs

Pragmatic approach to solving the problem

Sketch out key data structures

Sketch out key algorithms

Discuss tech stack
 - programming language
 - libraries
 - OS and hardware
 - Services

Discuss the implementation time

Discuss extensibility

Discuss scalability

Discuss caching

Discuss testability

Discuss security

Discuss internationalization

Discuss code reuse

'''

'''
Decomposition

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


'''

'''
Parallelism

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

'''

'''
Caching

Compute something, store it and look it up at a later date

Great whenever computations are repeated

Great when a system is responding to the same request multiple times

Complications include updating the cache in the presence of many requests
 - can use a second cache and hot swap
 - if using a second cache then warm this up before swapping this in
'''