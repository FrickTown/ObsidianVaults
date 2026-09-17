1. Explain the notation <_S_,_s_> → _s'_, explain the concept of axioms, rules, premises, conclusions, side conditions.
*S* here means statement
*s* means state
*s'* means the state resulting from statement *S* being applied to state *s*
*Rules* explains how, given a set of *premises* related to state and statement, what *conclusions* can be drawn from them. Conditionals, or side conditions, are additional preconditions to allowing the conclusion to be drawn from the premises.  A rule is invoked by writing *premises above*, and *conclusions below* a solid line, with *conditionals to the right-hand side* of the line. 
Some rules are fundamental and do not require any premises, for example 
$$ [skip_{ns}] = <skip, s>\ \rightarrow\  s$$
(skipping an instruction while in the state s, results in s being unchanged)
This is an *axiom*, a fundamental truth, and it does not require a solid line.

2. Explain the rule $[while^{tt}_{ns}]$. What are its premises, conclusions, side conditions?
$[while^{tt}_{ns}] = $
3. Exercise 2.3, but with x having the value 12
4. Exercise 2.4
5. Exercise 2.7, except the proof.
6. Consider a new statement for _x_:=_a1_ to _a2_ do _S_, informally meaning that _x_ is assigned successive values beginning with _a1_ and ending with _a2_ and _S_ is executed once for each value of _x_. So s:=0;for x:=1 to 3 do s:=s+x adds the numbers from 1 to 3 in s.  
    What would be the value of s and x after each of these different statements? Can you imagine different choices? Motivate!!
    1. s:=0; for x:=1 to 3 do s:=s+x
    2. x:=3; s:=0; for x:=1 to 0 do s:=s+x 
    3. x:=3; s:=0; for x:=1 to x do s:=s+x
    4. s:=0; for x:=1 to 3 do (s:=s+x; x:=x+1)