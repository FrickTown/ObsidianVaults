# Delays
#PropagationDelay 
- Time for bit to *propagate* from one end of link to other
$$
d_{prop} = d/s
$$
Där $s = c = 3*10^{8} m/s$ och $d$ är länkens fysiska längd.

#TransmissionDelay
- Time for source to put all bits on communication interface
$$
d_{trans} = L/R
$$
Där $L$ är paketets *längd i bitar* och $R$ är länkens *data rate*

#QueueingDelay
- Time to wait to be transmitted on a link. *Dependent on number and size of earlier arriving packets already in queue*
- Increases exponentially with #TrafficIntensity 

#TrafficIntensity
$$
I = La/R
$$
Där $L$ är paketets *längd i bitar*, $a$ är hastigheten med vilken ett paket anländer till länken $[s^{-1}]$ , vilket medför att $La$ är *traffic load*. $R$ är länkens *data rate*.
Traffic load mäter alltså hur över/underarbetad en nod är.

#ProcessingDelay
- Time to examine packet's header, determine destination, etc.
- In this course: 
$$ d_{proc} \rightarrow 0$$

#NodalDelay
- The sum of all delays
$$d_{nodal} = d_{proc}+d_{queue}+d_{trans}+d_{prop}$$

#RTT
- Round Trip Time
$$RTT \approx 2 * (d_{proc}+d_{prop}+d_{queue})$$
