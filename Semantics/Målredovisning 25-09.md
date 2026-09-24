# Goal 32
## Computation
$$
[comp_{ns}] \ \ \ \ \  
\frac
{\langle S_{1}, s\rangle \rightarrow s', 
\langle S_{2}, s' \rangle \rightarrow s''}
{ \langle S_{1};S_{2}, s \rangle \rightarrow s''}
$$
- $\langle S_{1}, s\rangle \rightarrow s'$
	- Låt $S_{1}$ vara ett statement som, när det appliceras på tillståndet $s$, resulterar i tillståndet $s'$
- $\langle S_{2}, s' \rangle \rightarrow s''$
	- Låt $S_{2}$ vara ett statement som, när det appliceras på tillståndet $s'$, resulterar i tillståndet $s''$
- $\frac{}{ \langle S_{1};S_{2}, s \rangle \rightarrow s''}$
	- Då kan vi dra slutsatsen att $S_{1}$, följt av $S_{2}$  applicerat på tillståndet $s$, resulterar i tillståndet $s''$
## While True
$$
[while^{tt}_{ns}] \ \ \ \ \  
\frac
{\langle S, s\rangle \rightarrow s'\  
\langle while\ b\ do\ S, s' \rangle \rightarrow s''}
{ \langle while\ b\ do\ S, s \rangle \rightarrow s''}\ \ \ \ 
if\  \mathcal{B}
$$
