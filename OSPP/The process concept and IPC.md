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
11. *How many times does fork return?*
Twice, once in the parent and once in the child.
12. *What are the possible return values of fork?*
-1, indicating an error with forking, 0, indicating that this process is the child that was just created, or a positive integer, which is PID of the child process that the parent receives. 
13. *After calling fork, how can the program know if it is executing in the parent or in the child*
As explained in 12, the return value from fork will be 0 in the child, and a positive integer PID (the child's PID) in the parent.
14. *What is the purpose of the exit system call?*
The exit system call marks a termination point of a process, allowing us to send an exit code to the parent process.
15. *What is the purpose of the exec family of system calls?*
Exec-esque system calls allows processes to completely change their currently executing program. This is necessary to run a child process that runs a separate program after fork()ing, for example. 
16. *When calling a function or invoking a system call, normally execution will return back to the caller, possible with a return value. Is this true for the exec family of system calls? Justify your answer.*
No. Exec will replace the process' currently running program entirely, meaning the exec call will not have anything to return to. It will start at instruction 0 of a new program instead.
17. *What is the purpose of the wait system call?*
The wait syscall stalls the program, and waits for (one of) its child process to finish and return an exit code before continuing.
18. *What is the purpose of the zombie process state? When does a process become a zombie?*
A process becomes a zombie when it has finished executing, but its parent has not yet wait()ed for it, meaning its return code has not been observed. The purpose of a zombie process is that its memory can be freed entirely, but still be able to give its data to its parent if the parent requests it.
19. *What is the purpose of signals?*
Signals allow processes to communicate, both asynchronously and synchronously.
20. What are the limitations of signals?
21. What happens when a process receives a signal?
22. *Explain the file descriptor concept.*
A process generally has three file descriptors, standard input (STDIN), standard output (STDOUT), standard error (STDERR). 