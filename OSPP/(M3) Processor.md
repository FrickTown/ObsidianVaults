# Seminar Questions
#### Different types of scheduling
1. *What is the overall purpose of the the short-term scheduler (aka CPU scheduler)?*
The CPU scheduler's job is to balance CPU time between ready jobs. It tries to keep the system responsive, by looking at priority set by the job scheduler, CPU burst time, and waiting time. 
2. *What is the overall purpose of the long-term scheduler?*
The job scheduler's purpose is to decide the viability of a new process, estimating its runtime, memory needs and IO needs. It may assign priority to new processes, determining how the short-term scheduler manages it later.
3. *What is the overall purpose of the medium-term scheduler?*
Schedules jobs based on resource requirements.
Swapping status of jobs, who becomes suspended waiting for IO.
#### Scheduling criteria
1. *Define the following scheduling criteria: CPU utilization, throughput, turnaround time, waiting time and response time. For each metric, state whether the goal is to minimize or maximize the metric.*
	- CPU Utilization = Percentage active usage of the CPU, as opposed to being idle. ⬆️
	- Throughput = Number of processes completed per time unit ⬆️
	- Turnaround time  = Total time taken for a process from creation to completion ⬇️
	- Waiting time = Process' total time spent in the waiting queue ⬇️
	- Response time = Time between request and first response ⬇️
#### Classification of processes
1. *What is meant by CPU burst? What is meant by I/O burst?*
The time a process uses the CPU before it is not ready anymore.
Time time a process waits for I/O before it is ready again.
2. *What characterizes a CPU bound process? What characterizes an I/O bound process?*
CPU bound processes are bottlenecked by CPU, and so would be faster if the CPU was faster. I/O bound processes are bottlenecked by I/O, for example, hard disk vs ssd.
3. *What would happen if there was a large majority of CPU bound processes in the ready queue?*
Increased CPU utilization
4. *What would happen if there was a large majority of I/O bound processes in the ready queue?*
Potential competition over I/O, which depending on the algorithm used for scheduling, could cause wait times. 
5. *How can a good balance between CPU bound processes and I/O bound processes in the ready queue be maintained?*
6. *What characterizes an interactive process?*
Continuous interaction between user and computer, e.g. a prompting program that asks the user multiple questions.
7. *What requirements on CPU scheduling does interactive processes impose?*
It requires being able to set processes to waiting and interrupts.
8. *What characterizes a batch process?*
A batch process requires all data to be provided before execution. No interaction necessary from execution to completion
#### Scheduling dispatch
1. *What is meant by scheduler dispatch?*
The scheduler determines which process is should be allocated to the CPU. The dispatcher performs the context switch for the next ready process.
2. *What actions are taken during a scheduler dispatch?*
Running process' CPU context is saved in the process' PCB. The PCB is then moved to the waiting queue. The next ready process is moved into running.
3. *Define dispatch latency.*
The time it takes to perform the switch. This is wasted CPU time.
4. *Scheduler dispatch can be preemptive and nonpreemptive, define these terms.*
Preemptive means it is capable of halting ongoing processes and switching it with another in the ready queue, if it has higher priority.
Nonpreemptive means processes run until their burst is finished.
5. *Draw a diagram showing which process state transitions causes a preemptive respectively a nonpreemptive scheduler dispatch.*
#### Scheduling algorithms
1. *Explain the FCFS scheduling algorithm.*
Runs processes as they arrive to the short-term scheduler. FIFO
2. *Explain the convoy effect.*
 If one long process precedes several short ones, the short ones will have to wait. Traffic behind big truck.
3. *Explain the SJF scheduling algorithm.*
Shortest job first. May cause issues if a process is too long, it will be starved (postponed indefinitely). Also can't handle infinite loops.
4. *In what way is SJF optimal?*
Finishing the maximum number of cpu bursts in the shortest time, if estimates are accurate
5. *Explain the PSJF scheduling algorithm.*
Pre-emptive SJF. Can handle infinite loops, because preemptive algorithms allow for the dispatcher to swap the active job before the current job is completed. If a job of higher priority is in the ready queue, it will swap places with it.
6. *Explain the RR scheduling algorithm.*
The round robin algorithm defines a time quantum and only allows processes a CPU burst of that length. If the time limit is reached, the process is put at the tail of the ready queue. If a syscall happens, it surrenders to the waiting queue as usual. 
7. *In general, what can be said about turnaround time and response time when comparing RR and SJF?*
```
Turnaround time = Time taken for a process from creation to completion
Response time = Time between request and first response 
```
RR will likely have a better response time on average. This is because a long job gets as much time on the processor as a short one, so even if a short job is in the back of the ready queue, it will respond in n\*q time where n is number of jobs before it in the queue, and q is the time quantum.
8. *In CPU scheduling, what is meant by starvation and ageing?*
Starvation means a process is ready, but never given CPU time. In a priority queue, there may be several higher priority processes preceding low priority process in the queue, causing the lower priority processes to be pushed back in the queue anytime a higher priority process enters the queue.
Aging can mitigate this. Processes that have not gotten a CPU burst for a long time will get increased priority, so that they have a better chance of reaching the front of the queue.
#### Multilevel queue scheduling
1. *What is the overall purpose of multilevel queue scheduling?*
If we have a lot of processes in the ready priority queue, we may need to perform a search every time to find the place in line for an incoming process. Multilevel queue scheduling just means we have a separate queue for each priority level. This gives a nicer structure and optimizes placing processes in line. We can timeslice among the queues to prevent aging, giving higher priority queues more time.
2. *In a ready queue for foreground processes, which algorithm of FCFS, SJF and RR would you choose. Justify your answer.*
Round Robin. This is because the user is interacting with these foreground processes, and the user does not want to experience hiccups. 
3. *What are the design objective of multilevel feedback queue scheduling?*
Optimizing line placement based on priority. 
4. *Explain how multilevel feedback queue scheduling works and how this relates to the design objectives.* 
#### Solaris and Linux
1. Explain how the Solaris dispatch table is used to dynamically change a the priority and time quantum (time slice) for a process.
2. Explain how a bitmap makes it possible for the Linux O(1) scheduler to find the highest priority process in constant time, independent of the the number of active tasks.
3. *The Linux Completely Fair Scheduler uses a red-black tree to keep track the processes in the ready queue. What is the time complexity of selecting the next process to run? What is the time complexity of inserting process (task) into the red-black-tree?*
Search in a red-black tree is O(log n)
Insert in a red-black tree is also O(log n)