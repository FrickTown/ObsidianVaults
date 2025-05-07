# IO Connections
### Differential Signaling
Two wires for serial connections, where one is used to pass the inverse signal of the other. *This removes noise efficiently by subtracting the two signals at the destination*.
### Buses vs p2p serial
- Too hard to keep wires synchronized with buses, different lengths and capacitance
- Replacement is SerDes (Serial/Deserializer)
### SerDes
Send bits continuosly and include the clock timing as part of the signal.
Signal becomes more complicated but the trade-off is worth it.
Uses more power though.

# Modern I/O interfaces
### UPI / HyperTransport p2p serial link
Communication between CPUs
### PCIe, p2p serial links
### SATA p2p serial link
### USB Ethernet external serial
### DIMMs are on buses
Commonly 2 DIMMs per bus

# Talking to I/O devices
### I/O Instructions
Like reg writing. Directly communicate with an address.
Downside: Limited commands and few devices available.
### Memory-mapped I/O
Portions of address space are mapped to the I/O devices
Reading and writing directly affect the device
Downside: Uses address space (limited)
### Direct memory access
Special hardware to take care of the execution of the r/w operations to and from I/O devices. The DMA unit offloads the I/O operations from CPU, which now only needs to make a request.

# Interrupts and polling
The OS needs to know when a device needs attention, when it's completed, and when there's an error.

We either use *polling* or *interrupts*.
### Polling
The CPU keeps checking the status of the device. Bad because the CPU is occupied with a menial task. Okay for small things like mouse/keyboard. 
### Interrupts
"Tell me when you're done, I'm doing something else meanwhile"
Needs to save processor states for interrupts when they occur and we jump to a service routine.
*We need to know which device generated interrupt*
- Vectored interrupt, which means every device has its own interrupt address.
- Status register, which is checked when an interrupt occurs and contains the address for the device that interrupted

*Priority*, how do we handle multiple interrupts?
An example is pressing a key while a disk is being read.
We can either *mask*, which disables interrupts from other devices entirely while one is in progress, or *nest*, where we take an interrupt within an interrupt.
If we miss an interrupt, we won't get the data.

### OS Responsibilities
OS ensures the I/O system is *shared* properly between devices, *causes* the interrupts, and manages drivers and state management.
Needs to be user friendly, through protection and abstraction, and high-performant.

# Ethernet 
Differential serial communication which divides data into packets.
Cyclic redundancy checksum (CRC) ensures data is not corrupted.
![[Pasted image 20250507121332.png]]
****An Ethernet packet***

**Collisions can occur if two devices transmit at the same time.**
- We detect the collision, by reading the data to see if another packet has corrupted it.
- We continue for 51.2µs, so that everyone sees that collision.
- We then wait for a random and increasing period of time and start again.

### We use network switches and buffer and route packages to the correct endpoints. This prevents collisions and simplifies network setup.

