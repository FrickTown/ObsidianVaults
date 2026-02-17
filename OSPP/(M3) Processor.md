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
1. *Define the following scheduling criteria: CPU uti-*
*lization, throughput, turnaround time, waiting*
*time and response time. For each metric, state*
*whether the goal is to minimize or maximize the*
*metric.*
#### Classification of processes
1. *What is meant by CPU burst? What is meant by I/O burst?*
The time a process uses the CPU before it is not ready anymore.
Time time a process waits for I/O before it is ready again.
2. *What characterizes a CPU bound process? What characterizes an I/O bound process?*
CPU bound processes are bottlenecked by CPU, and so would be faster if the CPU was faster. I/O bound processes are bottlenecked by I/O, for example, hard disk vs ssd.
3. *What would happen if there was a large majority of CPU bound processes in the ready queue?*
Competition 
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
1. What is meant by scheduler dispatch?
2. What actions are taken during a scheduler dis-
patch?
3. Define dispatch latency.
4. Scheduler dispatch can be preemptive and nonpre-
emptive, define these terms.
5. Draw a diagram showing which process state tran-
sitions causes a preemptive respectively a nonpre-
emptive scheduler dispatch.
#### Scheduling algorithms
1. *Explain the FCFS scheduling algorithm.*
Runs processes as they arrive to the short-term scheduler.
2. *Explain the convoy effect.*
 If several long processes precede a short one, the short one will have to wait.
3. *Explain the SJF scheduling algorithm.*
Shortest job first. May cause issues if a process is too long, it will be starved (postponed indefinitely). Also can't handle infinite loops.
4. *In what way is SJF optimal?*
Finishing the maximum number of cpu bursts in the shortest time, if estimates are accurate
5. *Explain the PSJF scheduling algorithm.*
Pre-emptive SJF. Can handle infinite loops, because preemptive algorithms allow for the processor to focus on other things before the current job is completed.
6. *Explain the RR scheduling algorithm.*

7. In general, what can be said about turnaround time and response time when comparing RR and SJF?
8. In CPU scheduling, what is meant by starvation and ageing?
#### Multilevel queue scheduling
1. *What is the overall purpose of multilevel queue scheduling?*

2. In a ready queue for foreground processes, which algorithm of FCFS, SJF and RR would you choose. Justify your answer.
3. What are the design objective of multilevel feedback queue scheduling?
4. Explain how multilevel feedback queue scheduling works and how this relates to the design objectives. Solaris and Linux
5. Explain how the Solaris dispatch table is used to dynamically change a the priority and time quantum (time slice) for a process.
6. Explain how a bitmap makes it possible for the Linux O(1) scheduler to find the highest priority process in constant time, independent of the the number of active tasks.
7. The Linux Completely Fair Scheduler uses a red black tree to keep track the processes in the ready queue. What is the time complexity of selecting the next process to run? What is the time complexity of inserting process (task) into the red-black-tree?
#### Solaris and Linux
1. Explain how the Solaris dispatch table is used to dynamically change a the priority and time quantum (time slice) for a process.
2. Explain how a bitmap makes it possible for theLinux O(1) scheduler to find the highest priority process in constant time, independent of the thenumber of active tasks.
3. The Linux Completely Fair Scheduler uses a red-black tree to keep track the processes in the ready queue. What is the time complexity of selecting the next process to run? What is the time complexity of inserting process (task) into the red-black-tree?