# Regularity of language
A language is regular if it can be contained in a finite amount of memory.
If the language satisfy any of the following:
## Recognizable by finite automaton
If a finite automaton (DFA, NFA) accepts exactly the strings in $L$
The automaton must have a finite amount of states, since this implies it has no unbounded memory.
## Describable with a regular expression
## Särskiljandesatsen
Om oändligt många strängar särskiljs av L, så är L ickereguljärt.
#### BEVIS: 
Om oändligt många strängar särskiljs av L så måste – enligt SATS 2.3 – en DFA för L särskilja oändligt många strängar. Men en DFA kan bara särskilja så många strängar som den har tillstånd – ändligt många således.

# DFA Formal Definition
![[Pasted image 20260128215823.png]]
![[Screenshot_20260128_220127.png]]
# Regular expressions
![[Pasted image 20260130170024.png]]
[[Automataboken.pdf#page=23|Automataboken, page 23]]

# Regular languages
A regular language is one that can be expressed with a finite automata or a regular expression.
#### Pumping lemma
If a language is regular, then every string has a segment that can be "pumped" (concatenated on the end) indefinitely (if they are at least as long as a certain length $P$).
$$
\begin{enumerate}

For\ each\ i > 0, xy^{i}z \in A

\end{enumerate}
$$