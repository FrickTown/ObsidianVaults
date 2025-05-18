# Part 1
1. *What is the hit rate? Why do we see this value?*
	- The hit rate is 0%, since we cannot fit the whole array into cache, every index above 512 will start to replace the first half with the second half. When we loop next time, we will again replace the second half with the first half, and this repeats.
2. *How many misses do we have in total? How many of them are compulsory misses? Explain your answer.*
	- 2560, all are compulsory. We cannot fit the whole array (1024 bytes) into cache (512 bytes)
3. *Change the block size from 4 bytes to 8 bytes but keep the cache size to 512 bytes (reduce the number of blocks accordingly). How are the compulsory misses affected when Block Size is changed from 4 bytes to 8 bytes? Is there any change, why/why not?*
	- They remain the same. Now we can just fit two words in a block, but we still cannot fit the whole array into cache, so the problem persists.
4. *Change the block size back to 4 again, and change the mapping from “direct mapping” to “2- ways set associative”? Cache size should be 512 bytes again, change the number of blocks accordingly. Is there any change in number/types of misses comparing “direct mapping” vs. “2-ways set associative” of the same size, why/why not?*
	- No, there is no change. We still have a 512 byte size. We have reduced the number of rows to access, likely to a performance benefit. But we still cannot fit the whole array, and due to LRU replacement policy, we will never luck out. 
5. *With the block size of 4, experiment with different cache sizes by changing the number of blocks. Try with both “direct mapping and “2-ways set associative”. How the hit rate is improved? At which point changing the cache size does not affect the hit rate?*
	- ![[Pasted image 20250515163648.png]]
	- ![[Pasted image 20250515163312.png]]
	- ![[Pasted image 20250515163338.png]]
	- ![[Pasted image 20250515163555.png]]
6. *At this “optimal” cache size (question 5) with the “direct mapping” option, what hit rates do you obtain by changing the block size? Try & report the hit rates with the sizes 4 bytes, 8 bytes and 16 bytes (you should keep cache size the same).*
	- ![[Pasted image 20250515164340.png]]
	- ![[Pasted image 20250515164410.png]]
	- ![[Pasted image 20250515164452.png]]
	- ![[Pasted image 20250515164519.png]]
	- ![[Pasted image 20250515164541.png]]
7. *Show how the achieved hit rate (as shown by simulator) can be computed (by hand) for different block sizes for the “optimal” cache size you found in question 5. Hint: what is the size of a single element in the array?*
	- 1024 / 
# Part 2
