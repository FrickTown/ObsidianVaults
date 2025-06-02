In the brain, we have neurons that fire off a signal when their internal charge reaches a threshold. This signal is then influencing the neuron's neighbor, potentially causing it to send a signal to its neighbors.
A neural network simulates this, and is a complex web of fairly simple constituents.

Fundamentally these are
- Nodes, often represented visually as circles, that contain a value
- Weights, represented as lines, that describe one node's influence on another

This picture can be viewed as a bunch of values between 0 and 1, representing the lightness of each pixel. This will be the first layer of the neural network: 144 nodes between 0 and 1.

Now, we draw a line from a node to all of it's neighbors in the next layer.
Biases, which are often manually tuned to make some nodes more influential
The value of nodes are normalized, meaning they contain a value between 0 and 1. 