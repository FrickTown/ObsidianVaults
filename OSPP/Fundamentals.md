# Quick notes
lui = Load upper immediate 
ori = OR immediate
li = lui + ori
srl and $sll = shift right/left logical
mfc0 = Move from coprocessor 0
eret = Exception return
# Exceptions
- Internal and synchronous
- Used for internal program errors (overflows, db0, bad address)
- A.K.A trap
# Interrupts
- Notifies CPU of external events
- Asynchronous

# Multiprogramming state transitions
![[Pasted image 20260125193320.png]]
# Questions
- In (Mips) Assembly, what are labels?
	Labels are intended for programmers to mark their code, but can also be used for jumping to specific parts of the code, without constantly adjusting the target address.
- What actions are unconditionally taken by the MIPS CPU when an exception/interrupt occurs?
	- EPC is stored in c0 \$14
	- Cause code is stored in c0 \$13
- How do you determine if an exception or interrupt caused the transition to the kernel entry point?
	- By checking bits 2-6 of the cause code. If they are 0, an interrupt occurred. Else, an exception occurred.
- In the original code you were given, the same exception was happening again and again and again in an infinite loop. Why? How to avoid this?
	- Because the EPC is the exact instruction where the exception occurred. Putting the PC back there when the exception has been handled means it will execute again. Manually adjusting the EPC by increasing by 4, for example, will ensure the causing instruction is skipped.
- When you run the system in Mars, why is the `$s0` register incrementing?
	- Because of the infinite_loop label jumping back to infinite_loop
- What pedagogical purpose do you think this incrementing loop serves?
	- The CPU is occupied in software, but an interrupt can still break that loop and cause other code to run. 
- For interrupts, how do you determine if it actually was a keyboard interrupt?
	- If bit 8 of the cause code in c0 \$13 is 1.
- Why do you think the exception code uses a 5 bit numeric field allowing for 32 different kinds of exceptions and interrupts uses 8 pending bits, one each for the 8 types of - interrupts only allowing for 8 types of interrupts and not 2^8 = 256 types of interrupts?
	- To allow for multiple interrupts to be activated simultaneously
- How are you able to know which key was pressed?
	- The key ascii value is stored at address 0xffff0000(+4). This value is fetched and printed with a syscall.
