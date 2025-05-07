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
