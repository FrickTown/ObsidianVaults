 # Seminar Questions
## Memory management
1. *When creating a new process the operating system must allocate memory for two structures, name and explain the purpose of these structures.*
- The PCB, or process control block
- Process memory image
- A file descriptor table

2. *One option is to allocate the memory needed by a single process contiguously in a sequential sequence of physical memory addresses. Describe two major problems with this approach.*
Can lead to external fragmentation.
Physical memory addresses may be used by other processes.
Overflows can lead to unintended access of memory blocks 

3. *Explain what is meant by memory compaction.*
Blocks of memory that may once have been directly adjacent to one another contiguously, may find themselves without neighbors if their neighbors are deallocated. Compaction simply pushes memory blocks together. This is faster for reading and could allow for big blocks to be allocated whereas they previously could not.

4. *Explain the purpose of logical memory addresses and how logical memory addresses relates to physical memory addresses.*
Logical memory addresses ensure that programs don't have to specify exactly at which addresses in the physical memory its data should end up. It is instead relative to the process. 

5. *Explain why compaction cannot be done without introducing logical memory.*
Because processes using physical memory cannot be moved without altering the program itself. Logical memory address 0x4 can be anywhere, but physical memory address 0x4 is fixed.

6. *What is the meant by external fragmentation?*
External fragmentation refers to there being space between the memory blocks of processes that is not being used. There is space, but it is not contiguous. This is different from internal fragmentation, where memory that is not actually being used by a process is still reserved for that process.

7. *What does the acronym MMU stand for and what is the purpose of the MMU?*
The memory management unit is responsible for translating between logical memory addresses to physical ones. In paged memory management, it also maps pages to frames. 

8. *In the below figure, a simple MMU is shown.* 
	1. *a) Explain the purpose of the relocation registers.* 
The relocation register keeps track of the offset we need to add for each process' logical address to get the physical one. 
The limit register keeps track of the limit in physical memory for the process.
	2. *b) What problems could occur if the check against the limit register was omitted?*
We could start writing and reading memory from neighboring memory segments.
<span style="display: flex; justify-content: center;"><img style="width:100%" src="Pasted image 20260304211439.png"</img></span>

9. *What is the purpose of virtual memory?*
A total contiguous memory span consisting of both swap space and RAM, giving the illusion of more memory than is actually available. Pages may be swapped in and out of storage. 

10. How is a virtual memory address space similar to a logical address space and how are they different?

11. *What problem with contiguous memory allocation is solved by introducing a page table?*
External fragmentation causing memory blocks to not be allocatable, not due to lack of free memory, but due to lack of free contiguous memory.

13. *How are pages and frames similar? How are they different?*
They are similar in that they are the same size in bytes. They are different in that frames are what the physical ram is divided up into contiguously, while pages are what the logical memory is divided up into, to be mapped onto frames.

14. *What is the purpose of the page table?*
Its purpose is to map pages to frames and vice versa. 

15. *With a logical address length of 16 bits and a page size of 8K byte, a process in the system gets the following page table: *

| Page  | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| Frame | 4   | 3   | 7   | 1   | 2   | 5   | 6   | 0   |

*Compute the physical addresses for the following logical addresses:*
	a. `0x0F51` 
	$(256 * 15) + (16 * 5) + (1 * 1) = 3921 =$`0000111101010001`
	=> Page 0 (000), Frame 4 = 8192 * 4
	=> 0x8000 + 0xF51 = 0x8F51
	b. `0xA619` 
	$(4096 * 10) + (256 * 6) + (16 * 1) + (1 * 9) =$`1010011000011001`
	=> Page 5 (101), Frame 5 = 8192 * 5
	=> 0xA000 + 0x619 = 0xA619
	c) `0x86BC` 
	$(4096 * 8) + (256 * 6) + (16 * 11) + (1 * 12) =$`1000011010111100`
	=> Page 4 (100), Frame 2 = 8192 * 2
	=> 0x4000 + 0x6BC = 0x46BC
	d) `0x70AD` 
	$(4096 * 7) + (256 * 0) + (16 * 10) + (1 * 13) =$`0111000010101101`
	=> Page 3 (011), Frame 1 = 8192 * 1
	=> 0x2000 + 0x0AD = 0x20AD
presented here in hexadecimal form. Your answers should be in hexadecimal.
Hint: convert each logical address to a binary number, detect what bits should be associated with the page and convert them back to the physical address using the page to frame translation table above.

16. *Why is the translation lookaside buffer (TLB) introduced?*
To reduce the time needed to lookup page tables. It acts as a cache for recently or often accessed pages. Can be read in parallel. 

17. *Draw a diagram showing how an logical (or virtual) address as seen by the CPU is translated to a physical address using a page table and TLB.*
<span style="display: flex; justify-content: center;"><img style="width:85%" src="Pasted image 20260305070955.png"</img></span>
18. *What problem is solved by introducing hierarchical page tables?*
In systems with quite big address-spaces, the page table itself can become quite large, and trying to allocate it in memory contiguously may cause the same issues that we were trying to solve with pages in the first place. Hierarchical page tables divides the page tables into multiple, smaller tiers, circumventing the need for a contiguous block of memory to contain the data.

## Files and file systems
19. *What is meant by persistent data storage?*
Unlike volatile data storage, which loses its contents when it loses power, persistent data is saved even without power. It persists between power cycles.

20. *A file is the smallest unit of secondary storage. Explain what this means.*
Data cannot be freely written to storage. It needs to be contained within a file.

21. *Describe the relation between the system-wide open file table and the per-process open file table.*
The system-wide open file table contains a copy of the file control block of each open file, which points to the data blocks of a file. On an open() syscall being made, the system looks in the system-wide OFT to see if the file is already open, if it isn't it is put in the system-wide OFT and then an entry for the file is created in the per-process OFT.

22. *What is the purpose of the directory structure?*
It maps FCB numbers to file names.

23. *To store a file on secondary storage, blocks of storage must be allocated to a file. What is meant by random access time in relation to secondary storage access?*

24. *What are the limitations of contiguous block allocation?*
It wastes space due to external fragmentation, and there is no guarantee that files can grow. 

25. *Discuss and compare random access time for*
	1. *linked allocation* 
	Files are a linked list of disk blocks. No random access, search time is linear.
	2. *FAT*
	The file access table simply is a copy of the hard drive without the data, only the block numbers. In this way, linearly searching through the FAT is faster, since there is less data to search. Even faster if cached in memory, which linked allocation cannot do. 

27. *Discuss the pros and cons of indexed block allocation.*

28. *Why does the Unix inode uses direct, indirect, double indirect and triple indirect data blocks?*