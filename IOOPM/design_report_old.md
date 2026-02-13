# Design Report


Reference counting can be described as simply keeping count of the number of references to an object. We do this by
deferring any direct memory allocation for an object (using malloc) to an allocation function, which puts a little
counter right before the object in memory. In addition to a counter, we also need a reference to a destructor function
to be called when the counter reaches 0. So we really need a little struct before the object. We define it as such:
```c++
typedef struct ref_counter {
    unsigned int count;
    void *data;
    function1_t destructor;
} ref_counter_t;
```
When we previously would `malloc` or `calloc`, we now use a function defined in ref_count.h `allocate()` or `allocate_array`. These functions return a void pointer, meaning it is generic, and will be interpreted as whatever the user needs it to be, depending on the context. The end user will never need to know about the ref_counter struct that sits atop of the object. 

## First iteration
Our original system design was quite minimal:
![](FooBarnen_Design_v0.1.png)
The reasoning for this is naturally because we were unable to predict some of the obstacles we'd encounter in
implementing the reference counter. We mostly just needed a reasonable file structure so that we could divide
the workload into discrete parts, so that we could work simultaneously without version control conflicts.


We decided on these three subdivisions of RC.h (which is the .h file that was handed out, later renamed ref_counter.h)
based on a separation of concerns. The reasoning went:
- `allocate`, `allocate_array` and `deallocate` all manage the actual memory allocation and deallocation, and were
therefore bundled together in a file named `allocation.c`.
- `retain`, `release`, and `rc` all manage the "count" value of a ref_counter_t object, so they were defined in a
file named `ref_counter.c`
- `cleanup`, `shutdown`, `get_cascade_limit` and `set_cascade_limit` do not fit into the other categories, and pertain
to the overarching functionality of the reference counter, so these were put in a file called `manager.c`


After getting the fundamentals working, we needed to think about:
- A hash table containing the pointer offsets for various object types
- A linked list containing any objects with zero references but that are yet to be deallocated


Therefore, we updated the system design to the following:

## Second iteration
![](FooBarnen_Design_v0.2.png)

The reasoning here was that the zero-ref list will need to be used by at least two of the files. Calling `retain()` on an 
object with zero references implies it no longer has zero references, and so needs to remove an element from the list.
Calling `cleanup()` will clear the list, and therefore needs to be able to reach it. We define the list as a common
(extern) variable in the `ref_counter_t.h` file, which includes the `linked_list.h` file. We can initialise the list
whenever we first need to put something in it.


Since the pointer offset hash table is really only relevant for `allocate` and `deallocate`, it can be alone in requiring
the hash_table.h file. 

However, in implementing type allocations and zero-ref stack, we encountered multiple issues, and we had a hard time placing these new 
features into already esablished modules. We needed several more files. This resulted in another rework to the design diagram:

## Third (and final) iteration
![](FooBarnen_Design_v0.3.png)

### Zero-ref stacked
The zero-ref stack is no longer a linked list. This was to prevent strange feedback loops, and keeping the zero_ref_counter itself out of memory management. It is instead a stack-like structure that can push and pop onto it. The reasoning is that if you allocated an object, you are likely to immmediately retain it, meaning
it will be at the top of the stack, so you can quickly pop it (it's not a true stack, since items other than the top can be removed as well).

When an object is allocated, it is automatically added to the zero_ref stack, since it has no references yet. Additionally, `allocate()` and `allocate_array()` both clear the zero-ref list whenever they are called. When an object with zero references is `retain()`ed, it is removed from the zero-ref list. Therefore, it is vital that one retains an object they have just created, before trying to allocate another object. 

```c
// [BAD]
char* x = allocate(sizeof(char) * 10, NULL); // x is in the zero-ref list
char* y = allocate(sizeof(char) * 10, NULL); // y is the the list, x is now freed
retain(x); // Crash
retain(y);
puts(*x);

// [BETTER]
char* x = allocate(sizeof(char) * 10, NULL); // x is removed from zero-ref list
retain(x); // x is removed from zero-ref list
*x = 'f';
char* y = allocate(sizeof(char) * 10, NULL); // y is removed from zero-ref list
retain(y); // y is removed from zero-ref list
puts(*x); // Prints 'f'

``` 

**In some cases, for example, when adding an item to a linked list, you can expect the linked list to retain it. So calling retain() is not always necessary.**


ref_counter.h now defines macros that execute functions defined in type_registration.h, and implemented in type_registration.c. We want to keep the number of files that an end user needs to import to an absolute minimum: ref_counter.h exclusively. We also don't want to clutter the ref_counter.h file, so this requires further modularization.

```c
typedef struct test2 {
    int* p1;
    int padding;
    float padding2;
    char* p2;
}test2_t;

register_type(test2_t, p1, p2); // Creates an entry in the type registry {"test2_t" : [0, 24]}
test2_t *temp = allocate_from_type(test2_t); // Allocates memory required for a test2_t 
                                            // and sets it type to test2_t
```

When we allocate from type, we save the offsets in a hash table, with a type name as its key. This also means that the ref_counter_t type needs an additional field, so that when it is deallocated, it has something to look up in the type registry, namely:

```c
#pragma pack(1) // Prevent padding, reducing size from 32 bits to 25
typedef struct ref_counter {
    uint8_t count; // 8-bit counter, only 1 byte instead of 8 byte
    void *data;
    function1_t destructor;
    char *type; // New addition
} ref_counter_t;
```

This brings our total header size to 25 bytes, with #pragma pack(1) removing the padding between the count and data fields. 
The k-value for the implementation is as follows:
```INI
[Worst case]
Size of ref_counter_t = 25 bytes
Worst case k (memory requested is 8 bytes) = (25 + 8) / 8 = 4.125 

[make demo_memtest]
Memory requested in allocations: 4370 Bytes
Memory actually allocated: 7070 bytes
k = 7070 / 4370 = 1.617

```
These values were acquired by running our demo-program and counting any bytes requested in the `allocation()` functions.

After having fully implementing this third system design, our reference counter now achieves all the promised features.
