## General structure
32 general registers, ***$0*** through ***$31***, and also special registers ***hi*** and ***lo***,
## Commands
### Arithmetics
#### add R1, R2, R3
Adds *R2* and *R3* together and assigns the value to *R1*.
#### sub R1, R2, R3
Subtracts *R3* from *R2* and assigns the value to *R1*.
#### addi R1, R2, X
Immediately adds a value X to *R2* and assigns the value to *R1*.
#### mult R1, R2 (and multu, for unsigned)
Multiplies *R1* with *R2*, saves the 32 most significant bits in hi, and the 32 least significant bits in lo.
Use ***mfhi $X*** and ***mflo $X*** to move from these registers to register \$X.
#### div R1, R2 (and divu, for unsigned)
Divides *R1* by *R2* and saves the remainder to ***hi*** and the quotient to ***lo***
### Logical
#### (and / or) R1, R2, R3
Performs and/or with R2 and R3 and assigns the value to R1.
#### (andi / ori) R1, R2, X
Performs and / or with R2 and X, and assigns the value to R1.
#### (sll / srl) R1, R2, X
Shifts R2 by X bits to the left or right, assigns the value to R1.

### Data transfer
#### lw R1, X
Loads a word from location X in memory, then moves it to registry R1
#### sw R1, X
Stores a word from R1 at location X in memory
#### li R1, X
Loads a word of value X immediately into R1



