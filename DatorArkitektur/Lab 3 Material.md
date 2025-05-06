*Q1: Why are we saving bits 20-16 and 15-11 of the instruction? How are they used, and why do we not save the whole instruction?*
These bits determine the write register, depending on the format of the instruction we either use 20-16 or 15-11 for the 5-bit reference to the register. 
If we were to save the whole instruction 
Because of the sign extension taking a bit of time, but we need to allow the next instruction 