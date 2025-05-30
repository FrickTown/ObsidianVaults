# Branch Delay Slot
A branch instruction needs to reach the MEM stage. We can detect this hazard in the ID stage, but this would require 3 NOPS afterwards.
This is okay, but slow.

We can add branch jump logic to earlier stages, but at best in a 5-stage pipeline we need *1 cycle* as a branch delay slot. This is not efficient.

If we have an instruction before the branch instruction, we can move it to the branch delay slot, to make it more efficient. 

In a processor with 15 pipeline stages we can't move the logic back as much. Which means we need more delay slots. These can't be filled as easily with earlier or later instructions.

<span style="display: flex; justify-content: center;"><img src="Pasted image 20250530161314.png"</img></span>

# Predicting branch not taken
We only know whether a branch is taken or not once we reach the MEM cycle.
If we assume that the branch is not taken, we can continue to execute the following three instructions instead of NOPing. 