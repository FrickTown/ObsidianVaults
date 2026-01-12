```c
#include <assert.h>
#include <string.h>

#define typename(x) _Generic((x), \
    int:     "int", \
    float:   "float", \
    default: "other")

int main(void) {
    int i;
    float f;
    void* v;
    assert(strcmp(typename(i), "int")   == 0);
    assert(strcmp(typename(f), "float") == 0);
    assert(strcmp(typename(v), "other") == 0);
}
```


```c
typedef struct
{
    unsigned int retainCount
    void       * data;
}

MemoryObject;
void * Alloc( size_t size )
{
    MemoryObject * o;
    char         * ptr;
    
    o              = ( MemoryObject * )calloc( sizeof( MemoryObject ) + size, 1 );
    ptr            = ( char * )o;
    ptr           += sizeof( MemoryObject );
    o->retainCount = 1;
    o->data        = ptr;
    
    return ( void * )ptr;
}

void Retain( void * ptr )
{
    MemoryObject * o;
    char         * cptr;
    
    cptr  = ( char * )ptr;
    cptr -= sizeof( MemoryObject );
    o     = ( MemoryObject * )cptr;
    
    o->retainCount++:
}

void Release( void * ptr )
{
    MemoryObject * o;
    char         * cptr;
    
    cptr  = ( char * )ptr;
    cptr -= sizeof( MemoryObject );
    o     = ( MemoryObject * )cptr;
    
    o->retainCount--:
    
    if( o->retainCount == 0 )
    {
        free( o );
    }
}
```

https://mailund.dk/posts/c-refcount-list/
