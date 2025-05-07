*Q1: Why are we saving bits 20-16 and 15-11 of the instruction? How are they used, and why do we not save the whole instruction?*
These bits determine the write register, depending on the format of the instruction we either use 20-16 or 15-11 for the 5-bit reference to the register. 
If we were to save the whole instruction 
Because of the sign extension taking a bit of time, but we need to allow the next instruction 

*Question 2: For each of the signals from the control circuit, explain why is it a write-back (WB), memory (MEM) or execution signal (EX).*
#### WB - Write Back, Infers writing back into registers at the end of a cycle.
- RegWrite, since its 1-bit value determines whether the data currently stored in "Write data" is to be written to a register.
- MemToReg, since its 1-bit value determines whether to pass a value loaded from memory into "Write data" input of registers.
#### MEM - Memory, the cycle segment where we are reading memory
