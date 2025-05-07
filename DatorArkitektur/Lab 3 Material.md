*Q1: Why are we saving bits 20-16 and 15-11 of the instruction? How are they used, and why do we not save the whole instruction?*
These bits determine the write register, depending on the format of the instruction we either use 20-16 or 15-11 for the 5-bit reference to the register. 
If we were to save the whole instruction 
Because of the sign extension taking a bit of time, but we need to allow the next instruction 

*Question 2: For each of the signals from the control circuit, explain why is it a write-back (WB), memory (MEM) or execution signal (EX).*
#### WB - Write Back, Infers writing back into registers at the end of a cycle.
- RegWrite, since its 1-bit value determines whether the data currently stored in "Write data" is to be written to a register.
- MemToReg, since its 1-bit value determines whether to pass a value loaded from memory into "Write data" input of registers.
#### MEM - Memory, the cycle segment where we are reading memory
- MemRead belongs to this cycle, sort of self-explanatory. Its 1-bit value determines whether the address passed to the RAM is to be read from
- MemWrite belongs to this cycle for the same reason. Its 1-bit value determines whether the address passed to the RAM is to be written to.
- Branch is not as self explanatory. However, it belongs in this stage because if we are jumping, we are definitely not writing back to a register, but the branch jump calculation depends on the EX segment being clocked. For this reason, it belongs to the segment after EX, which happens to be MEM.
#### EX - Execution signal, the cycle segment where calculations are made 
- RegDst determines how the destination register (if one is to be written to) is interpreted from the instruction (either bits 20-16 or bits 15-11). This is vital because in the next segment of the cycle, the "Write reg" is potentially written to. 
- ALUSrc determines if the second-source operand for the ALU is going to be Read data 2 or the sign-extended immediate. This is an EX signal because it needs to be determined before MEM, so that the ALU can calculate the memory address.
- ALUOp is an EX signal for similar reasons to ALUSrc. We need to have set up all necessary inputs for the ALU so that it can do its calculation in the next cycle segment.  
##  Test programs
```YAML
lw $t1, 0($zero)
sw $t2, 0($zero)
```
For each program, answer the following questions:
Question 3: What does the program do?
Question 4: If you execute the code on your pipelined processor, does it work? (Does it produce the
expected result?)
Question 5: If the answer to Question 4 is NO, explain why?
Question 6: If the answer to Question 4 is NO, change the code so it will work. (Hint: you can use the
online MIPS assemblera to compile new code and save it in your own .mem file to test.)