1. *What is meant by a process?*
A process is a running program that will execute fully and return a status code to its creator when it is finished. 
2. *A process needs at least two critical resources, name*
*these resources.*
A process control block (PCB), which is a data structure in the kernel which tells the cpu the vital info necessary to run and manage the process.
And a process image, which memory allocated for the program containing its memory segments and the instructions to run.
3. *Name and describe the various memory segments*
*used by a process.*
The stack, the heap, the text, and the data.
4. *A process can be in different states. Name and ex-*
*plain the purpose of each such state.*
- New, meaning it is newly created but not yet ready to run
- Ready, meaning it is idle and ready to be executed 
- Running, meaning its currently being executed
- Waiting, meaning it is currently awaiting data from another process
- Terminated, meaning it has finished executing or was prematurely terminated by a signal.
- Zombie, where it has been terminated and its memory freed, but the parent has not yet wait()ed on its child, so its return code is retained in the PCB.

5. *Draw a diagram showing how the process states are*
*related using directed arrows showing possible state*
*transitions.*
![[Pasted image 20260205213022.png]]
6. *What is the purpose of the PCB?*
The PCB exists to keep track of metadata related to a process.
7. *Give examples of data stored in the PCB.*
The process ID and state, the CPU context, I/O status.
8. *Explain how PCBs can be used to construct various*
*process queues.*
Through the states that processes can be assigned, we can determine ready/waiting queues. We can order the PCBs based on state and then through a queue linked data structure we can ensure fair wait times.
9. *What is the purpose of the fork system call?*
The fork system call creates a clone process of the currently running process. This can be used to execute different programs or parts of a program concurrently.
10. *What do we mean with parent and child?*
The parent is the process that made the fork system call. The parent has some connection to its child, and can wait for it to finish executing to get some data back.
11. How many times does fork return?
12. What are the possible return values of fork?
13. After calling fork, how can the program know if it
is executing in the parent or in the child