## Writing to caches
### Write-through
Anytime you write data to the cache, you *also write it to memory*
- Nice because we skip the dirty bit (memory always up-to-date)
- Bad because memory is slow

#### Allocate-on-write
Essentially just means ""
### Write-back
Write newly updated data *only into cache*, only write to memory on eviction.
- Nice because we save a lot of time writing to memory
- Bad because we need a dirty bit to keep track of data having been edited
