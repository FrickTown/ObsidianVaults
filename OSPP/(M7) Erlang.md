# Seminar Questions
## Functional programming
1. *In short, how is the functional programming paradigm different from the imperative programming paradigm?*
Everything happens through function calls. We also lack state.
2. *What is meant by the head and tail of a list?*
The head is the first element of the list, and the tail is the chain of elements that follow it.
3. *What is meant by a predicate?*
A predicate is a function that returns a boolean, evaluating whether an argument is truthy according to some condition.
4. *What is meant by arity?*
The number of arguments 
5. *What is meant by a higher order function?*
A function that takes another function as a parameter. 
6. *What is meant by an anonymous function?*
An anonymous function is an unnamed lambda expression.
7. *How does anonymous functions relate to higher order functions?*
Anonymous functions can be used as parameters easily. In fact, they can be defined inside the function call itself. 
8. *Four common operations on lists are: map, filter, zip, and fold. In brief, describe these operations.*
Map: applies a function on each element in a list
Filter: returns a list that contains only elements of a list that match a given predicate.
Zip: Given two lists, returns a list that contains alternating elements from each list. $[x_{1},y_{1},x_{2},y_{2}]$
Fold: Given a list and a function that accepts two elements, $x, y$, initially, $y$ will represent the last element and $x$, the second to last element. The next tick of the Fold function, the result of the function is given as $y$, and the next element preceding x is the new x. 

## Recursion
9. *In computer science, what is meant by recursion?*
Recursion is a function that calls itself.
10. *Why is recursion important in functional programming languages?*
Recursion is important because generally, loops do not exist, since we do not have state.
11. *What is meant by tail recursion?*
Tail recursion is when the last thing that happens in a recursive function is the recursive call.
12. *How does tail call optimisation work?*
Tail call optimisation works by, in the compiler, changing tail recursive functions into a loop. 
13. *Why is tail recursion important?*
Tail recursion is important because it can prevent a stack overflow.
## Message passing
10. *What is meant by synchronous message passing? What is meant by asynchronous message passing?*
Synchronous: Code sends a message and is blocked until answer
Asynchronous: Code sends a message and usually a callback function, and continues executing, breaking to run the callback function once a response is received.
## The actor model
11. *Describe the actor model for concurrency?*
The actor model allows for asynchronous concurrency. In the actor model, processes have identities and mailboxes, which means an actor can send messages to other, or their own, mailbox, 
12. *How is the actor model different from processes and threads?*

## Erlang
The questions about Erlang has been divided into
separate sections.
## Lightweight processes
13. *What makes an Erlang process lightweight compared to threads and processes in operating systems?*

14. *In Erlang, how can you create a new process?*

15. *Do Erlang processes share any memory?*

16. *How can a process get to know its own process id (PID)?*

## Message passing
17. *Explain the syntax for sending a message from one process to another process.*

18. *Explain the syntax for receiving a message.*

19. *What can be sent in a message?*

20. *Is sending a message blocking the sender?*

21. *Is receiving a message blocking the receiver?*

22. *Is message passing in Erlang synchronous or asynchronous?*

23. *If process A sends a message to process B process and wants that process to send some sort of result back, how can this be accomplished?*

## Stateful process
24. *How is it possible for process to maintain and change state?*

## Process supervision
25. *What is the effect of linking two processes?*

26. *What is the purpose of trap exit?*
## Hot code swapping
27. *Explain what is meant with hot code swapping (aka hot swapping or code replacement).*
Replacing parts of code that is currently running without aborting the process.
28. *In brief, explain how hot code swapping works in Erlang.*
