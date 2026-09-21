# TCP Congestion Control
1) *Why does TCP repeatedly increase the congestion window until it detects a problem (timeout or triple duplicate ACKs), then decrease it instead of finding an optimal maximum then staying there?*
2) *Why are there two distinct phases, one with an exponential increase in congestion window, and one with a linear increase.*
This is because an exponential increase is preferable at the start of the increase, since the sending rate is doubled for each successful MSS ack. But continuously 
3) *During congestion avoidance, the congestion window increases linearly, but upon receiving triple duplicate acks, why does the congestion window halve instead of decreasing linearly.*