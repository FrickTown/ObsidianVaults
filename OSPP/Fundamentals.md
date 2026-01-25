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
- 