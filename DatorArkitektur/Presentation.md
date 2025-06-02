In the brain, we have neurons that fire off a signal when their internal charge reaches a threshold. This signal is then influencing the neuron's neighbor's charge, potentially causing it to send a signal to its neighbors.
A neural network simulates this, and is a complex web of fairly simple constituents.

Fundamentally these are
- Nodes, often represented visually as circles, that contain a value
- Weights, represented as lines, that describe one node's influence on another

This picture can be viewed as a bunch of values between 0 and 1, representing the lightness of each pixel. This will be the first layer of the neural network: 144 nodes between 0 and 1.

Let's imagine the second layer being only 1 node.
![[Pasted image 20250602155113.png]]
Each line represents a value, describing how much its source node should influence the destination node. The value of the destination node is essentially just a summation of each source node's value multiplied by its weight.
![[Pasted image 20250602155456.png]]
We can also assign a "bias" to each destination node, essentially giving a minimal sum required for the node to be influential to its neighbors.

Because the value of nodes are supposed to be normalized, meaning they contain a value between 0 and 1, we plug this sum into a "sigmoid" function in order to constrain it.