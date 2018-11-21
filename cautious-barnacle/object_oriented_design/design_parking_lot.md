# Design parking lot

## Use cases/ Key performance indicators (KPIs)- 5 mins

- Customers can park car in space
- Customers can retrieve car from space
- Customers can pay for parking
- Customers can park for different amounts of time
- Customers can park many cars
- Space is appropriate for car
- Customers can enter and exit in many places

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

## High level design

### Core objects - 5 mins

- Key objects in the system

### Relationships between objects - 5 mins

- Which objects are members of other objects
- Do any objects inherit from other objects
- One to many relationships
- Many to many relationships

### Actions - 5 mins

- Walk through a use case with your current design
  - Are you missing any objects or relationships

## Bottlenecks - 5 mins

- Amount of traffic
- Amount of data
  - Move references to data, not data
- Reading data quickly
  - Fragment large data
- Writing data quickly
  - Fragment large data
- Decoupling
  - Large data
    - Don't co-locate large data with metadata
  - Separate out interfaces
    - Don't deliver an entire customer object for an email address
- Implementation time
  - If time to market is important this might affect some of your decisions

## Overview

- _Storage:_
- _Scalability:_
- _Security:_
- _Failure Cases:_
- _Debugging and Testing:_

### Storage and data model

### Scaling

### Security

### Resiliance to failure

### Debugging

### Testing
