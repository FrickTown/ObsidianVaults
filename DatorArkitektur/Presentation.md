In the brain, we have neurons that fire off a signal when their internal charge reaches a threshold. This signal is then influencing the neuron's neighbor's charge, potentially causing it to send a signal to its neighbors.
A neural network simulates this, and is a complex web of fairly simple constituents.

Fundamentally these are
- Nodes, often represented visually as circles, that contain a value
- Weights, represented as lines, that describe one node's influence on another

This picture can be viewed as a bunch of values between 0 and 1, representing the lightness of each pixel. This will be the first layer of the neural network: 144 nodes between 0 and 1.

Let's imagine the second layer being only 1 node.
![[Pasted image 20250602155113.png]]
Each line represents a value, describing how much its source node should influence the destination node. The value of the destination node is essentially just a summation of each source node's value multiplied by its weight.
![[Pasted image 20250602161638.png]]
We can also assign a "bias" to each destination node, essentially giving a minimal sum required for the node to be influential to its neighbors. This is what is usually tweaked manually, if anything.

Because the value of nodes are supposed to be normalized, meaning they contain a value between 0 and 1, we plug this sum into a "sigmoid" function in order to constrain it.

Doing this math for a single node is fine. But a complex neural network can have many thousands of nodes per layer. We can arrange all the necessary calculations going from one layer to the next as a matrix multiplication.
![[Pasted image 20250602161329.png]]
This is, again, why graphics cards are so viable for AI.

The way we establish all the weights, is not by hand. It is by randomizing the weights first, and then giving the neural network a bunch of labeled data. We give it an image, and we tell it what the last layer should be. And it will gradually change its weights until it consistently ends up with the expected results.

Once the network has been trained on a sufficient amount of data, it will hopefully be able to recognize images. 