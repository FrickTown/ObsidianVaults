Kongruensrelation innebär att olika element får ekvivalenta värden genom en viss operation.
Två kongruenta trianglar, t.ex, kan vara väldigt olika stora, eller till och med spegelvända i relation till varandra i det negativa planet, men ändå ha samma vinklar. Operationen som ger vinkeln är en konsekvens av ration av triangelns sidor. Modulo-operationer är en annan typisk operation som kan ge upphov till kongruensrelationer, element emellan.

# Sats
$$\begin{split} Antag:\\
&X_{1} \equiv X_{2} (mod\ m)\\
&Y_{1} \equiv Y_{2} (mod\ m)\\
Då\ gäller:\\
a)\ &X_1+Y_{1}\equiv X_{2}+Y_2\\
b)\ &X_1-Y_{1}\equiv X_{2}-Y_2\\
c)\ &X_1*Y_{1}\equiv X_{2}*Y_2\\
\end{split}
$$
### a)

### b)

### c) 
$$\begin{split}
&Bevis:\\
&X_1Y_{1} - X_{2,}Y_{2} = X_{1}Y_{1}- X_1Y_{2}+ X_1Y_{2}-X_2Y_2\\
& = X_1(Y_1-Y_{2)} + Y_2(x_{1} - X_2)
\end{split}
$$

# Delbarhetstest
$$\begin{split}
&Bestäm\ resten\ vid\ div\ med\ 8:\\
&a)\ 138637\\
&637 = 640 - 3 (mod\ 8)
\end{split}$$
# Kongruensekvationer
$a_{x}\equiv c (mod\ m)$

x **mod 5**

| **x**  | 0   | 1   | 2   | 3   | 4   |
| ------ | --- | --- | --- | --- | --- |
| **2x** | 0   | 2   | 4   | 1   | 3   |
x **mod 8**

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 3   | 6   | 1   | 4   | 7   | 2   | 5   |
Detta kan sammanfattas i en sats:

$$\begin{split}
&1)\ ax \equiv 1\ mod\ m\ är\ lösbar\ \textbf{omm}\ SGD(a,m) = 1\\
&2)\ ax \equiv c\ mod\ m\ har\ precis\ en\ lösning\ x\ mod\ m\ om\ SGD(a,m)=1\\
&
\end{split}$$
SGD(a, m) = 1 om |differensen| mellan a och m är ett primtal förutsatt att a och m inte är primtal själva.

SGD(4, 9) = 1 (9 - 4 = 5 => prim)
SGD(5, 16) = 1 (16 -5 = 11 => prim)
SGD(3, 82) = 1 (82 - 3 = 79 => prim)
SGD(2, 17) = 1 (17 - 2 = 16 =/=> prim) // a & m både primtal
SGD(7, 15) = 1 (15 - 7 = 8 =/=> prim) // a primtal
SGD(12, 37) = 1 (37 - 12 = 25 =/=> prim) // m primtal

Sammanfattat: 
- Om SGD(a, m) = 1 så är differensen primtal omm ***a*** och/eller ***m*** inte är primtal.
- Differensen är *inte* ett primtal om ***a*** eller ***m*** är primtal.
$$\begin{split}
&Lös\ 4x\equiv 1\ (mod\ 11)\\
& 
\end{split}$$
# Fermats lilla sats
$$\begin{align*}
Låt\ &p\ vara\ primtal\ och\ a\in\mathbb{Z} så\ att\ p\ x\ a\ \\
\quad &Då\ gäller:\\
&\quad a^{p-1} \equiv 1 (mod p)\\

\end{align*}$$

# Eulers phi-funktion
$$\begin{split}
&Låt\ m \in \mathbb{Z}\ och\ m >= 1\\
&Då\ är\  \phi(m)\ = antalet\ element\ i\ mängden\\
&\quad \{x\in\mathbb{Z}|1\le x \le m\  \wedge\ SGD(x,m) = 1\}
&\quad\\
&Vidare\ gäller\ att\ SGD(m_1, m_2) = 1\\
&\quad => \phi(m_1,m_2) = \phi(m_1,m_2)
\end{split}$$
$$\begin{split}
& Exempelvis: \phi(720) = \phi(2^{4}*3^{2}*5)\\
&
\end{split}$$

