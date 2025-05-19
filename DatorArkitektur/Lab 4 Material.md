# Part 1
1. *What is the hit rate? Why do we see this value?*
	- The hit rate is 0%, since we cannot fit the whole array into cache, every index above 512 will start to replace the first half with the second half. When we loop next time, we will again replace the second half with the first half, and this repeats.
2. *How many misses do we have in total? How many of them are compulsory misses? Explain your answer.*
	- 2560, all are compulsory. We cannot fit the whole array (1024 bytes) into cache (512 bytes)
3. *Change the block size from 4 bytes to 8 bytes but keep the cache size to 512 bytes (reduce the number of blocks accordingly). How are the compulsory misses affected when Block Size is changed from 4 bytes to 8 bytes? Is there any change, why/why not?*
	- The number of compulsory misses are technically halved, since we load two words at a time. However, the two words we load at the same time succeed each other *horizontally*, but we are reading the 2D-array *vertically*.  We still cannot fit the whole array into cache, so the problem persists.
4. *Change the block size back to 4 again, and change the mapping from “direct mapping” to “2- ways set associative”? Cache size should be 512 bytes again, change the number of blocks accordingly. Is there any change in number/types of misses comparing “direct mapping” vs. “2-ways set associative” of the same size, why/why not?*
	- No, there is no change. We still have a 512 byte size. We have reduced the number of rows to access, likely to a performance benefit. But we still cannot fit the whole array, and due to LRU replacement policy, we will never luck out. 
5. *With the block size of 4, experiment with different cache sizes by changing the number of blocks. Try with both “direct mapping and “2-ways set associative”. How the hit rate is improved? At which point changing the cache size does not affect the hit rate?*
	- At a block count of 256, a cache size of 1024, we get a 90% hit rate. It does not improve with larger cache sizes, since we can already fit the entire array of 64 * 4 words 
6. *At this “optimal” cache size (question 5) with the “direct mapping” option, what hit rates do you obtain by changing the block size? Try & report the hit rates with the sizes 4 bytes, 8 bytes and 16 bytes (you should keep cache size the same).*
With a cache size of 1024 and 2560 memory accesses:

| Block size (bytes) | Hit count |
| ------------------ | --------- |
| 4                  | 2304      |
| 8                  | 2432      |
| 16                 | 2496      |
7. *Show how the achieved hit rate (as shown by simulator) can be computed (by hand) for different block sizes for the “optimal” cache size you found in question 5. Hint: what is the size of a single element in the array?*
		MAC = Memory Access Count
$$\frac{MAC}{MAC - \frac{Cache\ size}{Block\ size\ (bytes)}}$$
# Part 2
1. *Does the hit rate improve? Why? (show computation)*
	- $$1 - \frac{4}{4} = 0$$
	- No, it is still 0%. This is because we still load words individually as we need them, but we will never need a word again before it has already been evicted for newer data.
2. *Change the Block Size to 8 bytes (keep the cache size the same, 512 bytes)? Does the hit rate improve? Why? (show computation)*
	- $$1 - \frac{4}{8}= 0.5$$
	- Yes. Because the block size is now 8 bytes, when we try to fetch a word in memory and the word is not there, we load it, and also the word succeeding it. This means that the next memory access is guaranteed to be a hit, promising a 50% hit rate.
3. *Change the Block Size to 16 bytes (keep the cache size the same, 512 bytes)? Does the hit rate improve? Why? (show computation)*
	- Yes, just like in question 2, since each block is now 16 bytes, we can fit 4 sequential words, guaranteeing a 75% hit rate.
4. *Change the Cache Size to 1024 bytes and Reset the Block Size to 4 bytes. What is the hit rate? Compute this hit rate by hand.*
	- $$\frac{Hit\ rate_{first} + Hit\ rate_{remaining}}{Iterations} = \frac{1*\frac{1}{2}+9*\frac{1}{1}}{10}$$
	- 90% hit rate. We will go through the full array once, loading each word and storing it in memory. This means we will miss the first 256 memory accesses. After the first pass we will have all data needed for the following 9 iterations.
5. *Change Block Size to 8 bytes (cache size is 1024 bytes now). What is the hit rate? Compute this hit rate by hand*
	- $$\frac{(256 * \frac{4}{8}) + 9 * 256}{256 * 10}$$
	- 95% hit rate. Just like in question 4, with dash of question 2, we have to pass over the entire array once to load all the data into memory. However, this time, since we're loading 2 consecutive words at a time, we halve the miss rate of that first pass.
6. *Change Block Size to 16 bytes (cache size is 1024 bytes now). What is the hit rate? Compute this hit rate by hand*
	- $$\frac{1*\frac{3}{4}+9*\frac{1}{1}}{10} = 97.5\% $$
	- Predictably, this yields a 97.5% hit rate.
7. *Can a perfect hit rate of 1.0 be achieved without changing the program? Why?*
- No. We will have to load the data from somewhere.  
