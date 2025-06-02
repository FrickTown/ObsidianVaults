## Multicore
### The power wall
We hit the powerwall because it's *too costly* to cool processors that have a certain power need.

The power for a transistor is $P = CV^{2}f$ where *C* is the capacitance, *V* is the voltage, and *f* is the frequency.

*Capacitance stays the same* because we increase number of transistors per chip as they get smaller.
Voltage is most effective way to reduce power but since *silicon has a threshold voltage* where it doesn't work properly we cannot reduce it more.
We* can't just increase frequency*, because it would increase the power.

***This is why multicore is a thing***. But not all programs are designed to make use of it.

## Parallel Difficulties

If a program can be computed 75% in parallel, and 25% in serial, the time the parallel part takes is negligible compared to the serial part. We rely on the serial part for a lot of setup so that we can divvy up the work for the multiple processors.
*The performance is limited by the serial part of your code*
$$Speedup=\frac{1}{(1-P)+\frac{P}{S}}$$
Where P = Parallel fraction, S = speedup for the parallel part.

We reach a plateau of speedu