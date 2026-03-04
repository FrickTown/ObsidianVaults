 # Seminar Questions
## Memory management
1. *When creating a new process the operating system must allocate memory for two structures, name and explain the purpose of these structures.*
- The PCB, or process control 
- A file descriptor table
1. *One option is to allocate the memory needed by a single process contiguously in a sequential sequence of physical memory addresses. Describe two major problems with this approach.*
2. Explain what is meant by memory compactation.
3. Explain the purpose of logical memory addresses and how logical memory addresses relates to physical memory addresses.
4. Explain why compaction cannot be done without introducing logical memory.
5. What is the meant by external fragmentation?
6. What does the acronym MMU stand for and what is the purpose of the MMU?
7. In the below figure, a simple MMU is shown. a) Explain the purpose of the relocation registers. b) What problems could occur if the check against the limit register was omitted?
8. What is the purpose of virtual memory?
9. How is a virtual memory address space similar to a logical address space and how are they different?
10. What problem with contiguous memory allocation is solved by introducing a page table?
11. How are pages and frames similar? How are they different?
12. What is the purpose of the page table?
13. With a logical address length of 16 bits and a page size of 8K byte, a process in the system gets the following page table: 

| Page  | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| Frame | 4   | 3   | 7   | 1   | 2   | 5   | 6   | 0   |

Compute the physical addresses for the following logical addresses:
	a. `0x0F51` 
	b. `0xA619` 
	c) `0x86BC` 
	d) `0x70AD` 
presented here in hexadecimal form. Your answers should be in hexadecimal.
Hint: convert each logical address to a binary number, detect what bits should be associated with the page and convert them back to the physical address using the page to frame translation table above.

15. Why is the translation lookaside buffer (TLB) introduced?
16. Draw a diagram showing how an logical (or virtual) address as seen by the CPU is translated to a physical address using a page table and TLB.
17. What problem is solved by introducing hierarchical page tables?
## Files and file systems
15. What is meant by persistent data storage?
16. A file is the smallest unit of secondary storage. Explain what this means.
17. Describe the relation between the system-wide open file table and the per-process open file table.
18. What is the purpose of the directory structure?
19. To store a file on secondary storage, blocks of storage must be allocated to a file. What is meant by random access time in relation to secondary storage access?
20. What are the limitations of contiguous block allocation?
21. Discuss and compare random access time for
	1. linked allocation 
	2. FAT
22. Discuss the pros and cons of indexed block allocation.
23. Why does the Unix inode uses direct, indirect, double indirect and triple  indirect data blocks?