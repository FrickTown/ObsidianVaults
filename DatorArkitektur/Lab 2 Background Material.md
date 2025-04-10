<span style="display: flex; justify-content: center;"><img src="Pasted image 20250408194242.png"</img></span>
<span style="display: flex; justify-content: center;"><img src="Pasted image 20250408194311.png"</img></span>
***TODO: Answer these questions:***
*Q1: What would happen if none of the outputs from the Type Decode unit was true?*
The Control Decode circuit would not be given an input?
*Q2: How could none of the outputs be true at any time, and what does this mean about your Type Decoder?*
How? Because there is not a case for every 6-bit number. This also means the type decoder is incomplete, there should at least be a default case, for error handling.
<span style="display: flex; justify-content: center;"><img src="Pasted image 20250408203130.png"</img></span>
<span style="display: flex; justify-content: center;"><img src="Pasted image 20250408204408.png"</img></span>

***TODO: Answer these questions:***
*Q3: Why doesn’t the truth table you filled in have an entry for 0011?*
Because the beq bit signifies a branch-operation, and the sw bit signifies a memory storing operation. None of the currently implemented functions involve writing to memory and branching.
<span style="display: flex; justify-content: center;"><img src="Pasted image 20250409133748.png"</img></span><span style="display: flex; justify-content: center;"><img src="Pasted image 20250410130637.png"</img></span>
***Q4: Write down for each cycle (until the program runs out of instructions) what value is in each used register and what value and register will be written to for each instruction.***

- `lw $t1, 0($zero)` Load 1 into $t1 
- `lw $t2, 4($zero)`Load 2 into $t2
- `lw $t1, 12($zero)` Load 4 into $t0
- `add $t3, $t1, $t2` Set $t3 to 1 + 2 = 3
- `add $t4, $t3, $t1` Set $t4 to 3 + 1 = 4
- `sub $t0, $t0, $t2` *Set $t0 to $t0 - 2*
- `or $t5, $t4, $t1` Set $t5 to logical or of **00000100 | 00000001** = 00000101 = 5
- `slt $t6, $t4, $t5` Set $t6 to boolean (4 < 5) = 1
- `beq $t2, $t0, loop` Loop if $t0 == 2

Code will load 4 into $t0 with `lw $t0, 12($zero)` and will then decrease $t0 by 2 with the `sub $t0, $t0, $t2`, which will cause `beq $t2, $t0, loop` to go to loop. Nothing else in the register list will change during the second pass, except the sub command will decrease $t0 by 2 yet again, causing beq to no longer loop.

| Reg | Cycle 1 | Cycle 2 |
| --- | ------- | ------- |
| $t0 | 4       | 2       |
| $t1 | 1       | 1       |
| $t2 | 2       | 2       |
| $t3 | 3       | 3       |
| $t4 | 4       | 4       |
| $t5 | 5       | 5       |
| $t6 | 1       | 1       |
***Q5: What is the value of the Write data and the Write reg when the beq instruction is executed? Why? Is this a problem?***
First pass
Write data = 0 (2 - 2)
Write reg = 8
Second pass
Write data = 2 (2 - 0)
Write reg = 8

This is because the branch instruction format also uses the 5-bit rt and rs addressing, just like the other register operations
![[Pasted image 20250410134813.png]]
Bit 21:25 is used to specify which register to write to (*Write reg*) and bit 16:20 is used to specify which register the data comes from, the value of which is stored in *Write data*.

beq reads the value of rs and rt and uses the values in the ALU, subtracting rt from rs to see if they are equal. The other circuits that parse the full 32 bit instruction still also read rs and rt, which means Write reg and Write data are set just as normal<

This is not a problem, because when the clock ticks the register list, RegWrite is 0, which means neither WriteReg or WriteData is relevant.