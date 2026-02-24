# Seminar questions 
#### Threads
1. *How do threads differ from processes?*
Threads are kind of like sub-processes. These are several program counters in a single process, executing different parts of the code concurrently. While they each have their own stack (in order to be able to call functions and such), they share everything else in their process.
2. *Why is it more “expensive” to create a new process compared to creating a new thread?*
A new thread is just a new program counter to keep track of. A new process requires the OS to allocate and load a process into memory, assign it to a queue, etc.
3. *In short, explain the many-to-one user level thread model. Also explain what happens if one of the threads makes a blocking system call in the many- to-one user level thread model.*
Threads can either be on user-level or kernel-level. Generally, a good way to balance this, is to have several user-level threads be bound to some amount of kernel-level threads. Many-to-one means several user-level threads are bound to a single kernel level thread. Since we only have one kernel thread, we can not run in parallell. One thread blocks all other threads if it performs a blocking syscall.
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
If a process is excluded by a lock long enough, it will never execute. It waits indefinitely to get to its critical section.
#### Software based synchronization
8. *What are the limitations of Petersson’s solution to the mutual exclusion problem?*
- Only works for two processes (although can be generalized for more)
- Software solution, meaning potential difficulties with getting it to work on modern architectures, due to memory reordering (an optimization on modern hardware, causing memory accesses to occur out of order)
#### Hardware support for synchronization
9. *Name two atomic CPU instructions that can be used to implement synchronization locks.*
TAS (Test And Set)
SWAP
10. How can spin locks be constructed using the two atomic instructions from above?
```c
volatile bool lock = false;
// TestAndSet sets a value to True, and then returns whatever value was there before.
while (TestAndSet(&lock)){
}
// Critical section
lock = false;

```
 
```c
volatile bool lock = false;
do {
	key = true;
	while(key == true)
		Swap(&lock, &key);
	// Critical section
	lock = false;
} while (true)
``` 
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
#### Deadlock
15. *Name and explain the four necessary conditions for deadlock?*
Mutual exclusion: only one task at a time can use a resource
Hold and wait: a task holding a resource is waiting for another resource that is being held by another task
No preemption: A resource cannot be voluntarily let go by a task
Circular wait: A depends on B depends on C depends on A
16. *Explain the differences between deadlock prevention and deadlock avoidance.*
Deadlock avoidance does not allow deadlocks to occur, instead checking before performing any action that may lead to a deadlock. This requires a priori information.
Deadlock prevention allows some of the deadlock conditions to occur, but at least ONE must never occur. 
17. *Explain how deadlock prevention can be used to prevent circular wait.*
By imposing a strict ordering on resources, and only allowing tasks to access resources in increasing order of their number. So you NEED to obtain the resource of lower order to even request one of higher order. <span style="display: flex; justify-content: center;"><img style="width:45%" src="Pasted image 20260224111140.png"</img></span> 
This means 4 NEEDS to request resource 0 before it asks for resource 4. 
18. *What conclusions regarding deadlock can be made*
*using a resource allocation graph (RAG)?*
- If a RAG is acyclical, there is no deadlock
- If it does contain a cycle:
	- If only one instance per resource type => deadlock
	- Several instances per resource type => possible deadlock
#### Dining philosophers
19. *Explain the Dining philosophers problem.*
5 Philosophers sit around a circular table, with a bowl of rice in the middle. They need two chopsticks to eat from the bowl of rice. There is one chopstick on either side of each philosopher, meaning there are 5 chopsticks, so not every philosopher can eat at the same time. They need to wait until both left and right chopstick is available. If every philosopher tries to pick up their right chopstick, no one can pick of their left chopstick, which causes a deadlock.
#### Barrier synchronization
20. Two threads A and B both executes a loop concurrently with each other. In the loop, Thread A prints A and thread B prints B.
![[Pasted image 20260224100021.png]]
	In the loops there should be a barrier such that the first thread to reach the barrier must wait for the other to also reach the barrier. Once both threads have reached the barrier the threads are allowed to continue with the next iteration. For each iteration the order between the threads should not be restricted. The following is an example of a valid trace of execution: ABBABA. The following is an example of an invalid trace of execution: ABBBAB.
	*Explain how two semaphores can be used to en force the two threads to have a rendezvous at the barrier after each iteration.*
We have two semaphores: $S_{1}$ and $S_{2}$, both are set to 1.
Task A waits on $S_{1}$ to pass the barrier, and is allowed to pass.
Task B waits on $S_{2}$ to pass the barrier, and is allowed to pass.
Task A arrives at the barrier, and signals $S_{2}$, setting it to 1. Task A waits on $S_{1}$ to pass the barrier.
Task B arrives at the barrier, and signals $S_{1}$, setting it to 1. Task B waits on $S_{2}$ to pass the barrier.
21. *Could two mutex locks be used as drop in replacements for the two semaphores when solving the barrier problem above, where you replace wait with lock and signal with unlock? Justify your answer*
No, not in my solution, because a mutex has specific ownership of a lock. Only the process that locked can unlock. But my solution relies on Task A being allowed to modify $S_{2}$, even though it did not lock it, Task B did.
#### Bounded buffer
22. *Explain how semaphores can be used to synchronize access to a bounded buffer.*
- One semaphore named *empty*, which will display the number of empty slots in the buffer. Producers must wait on this to be allowed to write. Consumers signal this when reading. **Init: size of buffer.**
- One semaphore named *data*, which will house the number of occupied slots in the buffer. Producers signal this after writing to buffer. Consumers must wait on this. **Init: 0. **
- One semaphore (or mutex), for r/w access. Must be obtained before modifying next_in or next_out.
<span style="display: flex; justify-content: center;"><img style="width:90%" src="Pasted image 20260224113527.png"</img></span>
#### Banker’s algorithm
23. *Is Banker’s algorithm an example of deadlock prevention or deadlock avoidance? Justify your answer.*
Avoidance. 
24. Consider a system with four tasks T0, T1, T2, T3 and four resources A, B, C, D. The initial state S0 for Banker’s
algorithm is defined by:
![[Pasted image 20260224113636.png]]
#### Priority inversion
23. *Use a figure to explain what is meant by priority inversion.*
<span style="display: flex; justify-content: center;"><img style="width:100%" src="Pasted image 20260224114023.png"</img></span>
24. *Explain how priority inheritance solves the problem with priority inversion*
Priority inheritance solves the problem by elevating the blocking, lower-priority task to the level of the task that is being blocked, so that medium does not preempt the task that holds R. 