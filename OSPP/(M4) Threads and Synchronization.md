# Seminar questions 
#### Threads
1. *How do threads differ from processes?*
Threads are kind of like sub-processes. These are several program counters in a single process, executing different parts of the code concurrently. While they each have their own stack (in order to be able to call functions and such), they share everything else in their process.
2. *Why is it more “expensive” to create a new process compared to creating a new thread?*
A new thread is just a new program counter to keep track of. A new process requires the OS to allocate and load a process into memory, assign it to a queue, etc.
3. *In short, explain the many-to-one user level thread model. Also explain what happens if one of the threads makes a blocking system call in the many- to-one user level thread model.*
#### Need for synchronization
4. *What is meant by an atomic operation? Give examples of non-atomic operations.*
An action that happens all at once, a totally uninterruptable action. 
5. *Define the following terms: Race condition, Datarace, Critical section and Mutual exclusion.*
 Race condition: One process is dependent on, for it, uncontrollable events.
 Datarace: Two or more processes trying to modify same data at once, and at least one is write.
 Critical section: A section of a program that requires some limited resource
 Mutual exclusion: Only one process is able to access some resource. One can not have a thing if another already has it.
 
#### Properties of lock operations
6. *What is meant by a spin lock? What is meant by busy waiting?*
Spin lock is any lock that causes a thread to loop until it is available. Busy waiting is CPU time given to simply waiting. The process is not waiting, only a thread. 
7. *In the context of mutual exclusion, what is meant by starvation?*
If a process is excluded by a lock long enough, it will never execute.
#### Software based synchronization
8. What are the limitations of Petersson’s solution to the mutual exclusion problem?
#### Hardware support for synchronization
9. Name two atomic CPU instructions that can be used to implement synchronization locks.
10. How can spin locks be constructed using the two atomic instructions from above?
#### Abstractions for synchronization
11. *What operations can be performed on a semaphore and how do these operations work?*
`wait()` which reduces semaphore count by one, and if the resulting count is less than 0, the process waits
`signal()` which increases semaphore count by one, and wakes up one process, if any is waiting.
12. *What operations can be performed on a mutex lock and how do these operations work?*
`lock()`
`unlock()`
13. *What is the difference between a mutex lock and a semaphore?*
A binary semaphore is somewhat to a mutex lock. A mutex lock is simply a boolean, that is set by a process that wants to use a resource.
A major difference is in a mutex, the process takes ownership of its lock, so only it can unlock the mutex again. A semaphore is just an integer for counting current accessors.
14. *When implementing semaphores and mutex locks, how can busy waiting be avoided?*
Busy waiting can occur, for example, due to priority inversion (i.e. a lower-priority process is keeping a higher-priority process from executing). Priority inheritance and preemption can solve this. 