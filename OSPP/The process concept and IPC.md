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
- New, meaning 
- Ready, meaning it is idle and ready to be executed 
- Running, meaning its currently being executed
- Waiting, meaning it is currently awaiting data from another process
- Terminated, meaning it has finished executing or was prematurely terminated by a signal.

5. Draw a diagram showing how the process states are
related using directed arrows showing possible state
transitions.