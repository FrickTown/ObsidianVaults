## Cache structure
### Tag
We store a tag in a block, telling us which memory address' data is contained in the block
### Data
The data contained in the block
### Valid bit
### Dirty bit (optional)
## Types of caches
### Direct-mapped
### Fully associative
Every block is read every read
### N-way set associative

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
