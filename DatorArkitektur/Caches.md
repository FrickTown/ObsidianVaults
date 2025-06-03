## Cache structure
### Tag (Mandatory)
We store a tag in a line, telling us which memory address' data is contained in the line's blocks
### Data (Mandatory)
The data contained in the block(s)
### Valid bit (Mandatory)
Ensures data contained in the block is written to by the CPU during this runtime cycle. If the PC has just been powered on, all valid bits should be set to 0, so that its value will not be interpreted.
### Dirty bit
0/1 depending on whether the data in the block has been edited since it was loaded from memory
## Cache sizing
Since the tag for a line is 30 bits, we want to make use of each tag as much as possible. Each line can therefore contain many blocks. Usually this count is *16 blocks*.
<span style="display: flex; justify-content: center;"><img src="Pasted image 20250528194311.png"</img></span>
## Types of caches
### Direct-mapped
Each address maps to one line in the cache. This is done using modulo. Address % Line-count = Tag.
This means we always know exactly which line to search. We check the line for the data we want using a single comparator.
Reasonable because we often want to use sequential data anyway.
### Fully associative
Every block is read every cache-read, using the same number of comparators as we have lines in the cache.
### N-way set associative
Allow non-sequential data to be contained on each line. For every N set we need N comparators.
## Writing to caches
### Write-through
Write *directly to memory*. Anytime we do write, we also write to cache.
- Nice because we skip the dirty bit (memory always up-to-date)
- Bad because memory is slow
#### Allocate-on-write
Essentially just means "If data is not already in cache when we write to memory, put it there". Because subsequent data access will be faster. 
### Write-back
Write newly updated data *only into cache*, only write to memory on eviction.
- Nice because we save a lot of time writing to memory
- Bad because we need a dirty bit to keep track of data having been edited
## Cache Performance
![[Screenshot_20250528_192843.png]]
