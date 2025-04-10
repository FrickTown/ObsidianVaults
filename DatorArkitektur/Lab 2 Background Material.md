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
Code will load 4 into $t0 with `lw $t0, 12($zero)` and will then decrease $t0 by 2 with the `sub $t0, $t0, $t2`, which will cause `beq $t2, $t0, loop` to go to loop. Nothing else in the register list will change during the second pass, except the 

| Reg | Cycle 1 | Cycle 2 | Final |
| --- | ------- | ------- | ----- |
| $t0 | 4 (-2)  | 2 (-2)  | 0     |
| $t1 | 1       | 1       | 1     |
| $t2 | 2       | 2       | 2     |
| $t3 | 3       | 3       | 3     |
| $t4 | 4       | 4       | 4     |
| $t5 | 5       | 5       | 5     |
| $t6 | 1       | 1       | 1     |
