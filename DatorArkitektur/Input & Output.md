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
