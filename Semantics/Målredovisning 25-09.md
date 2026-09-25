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
{\langle S, s\rangle \rightarrow s',\  
\langle while\ b\ do\ S, s' \rangle \rightarrow s''}
{ \langle while\ b\ do\ S, s \rangle \rightarrow s''}\ \ \ \ 
if\  \mathcal{B}[[b]]s = \boldsymbol{tt}
$$
- $\langle S, s\rangle \rightarrow s'$
	- Låt $S$ vara ett statement som, när det appliceras på tillståndet $s$, resulterar i tillståndet $s'$ 
- $\langle while\ b\ do\ S, s' \rangle \rightarrow s''$
	- Låt $S$, applicerat på tillståndet $s'$, resulterar i tillståndet $s''$ givet att $b$ håller
- $if\  \mathcal{B}[[b]]s = \boldsymbol{tt}$
	- Om booleska variabeln $b$ i tillståndet $s$ är sann
- $\frac{}{ \langle while\ b\ do\ S, s \rangle \rightarrow s''}$
	- Då kan vi dra slutsatsen att $S$, applicerat på tillståndet $s$, medan $b$ håller (det vill säga, är sann), resulterar i tillståndet $s''$. 
# Goal 34
```
x:=8;
while 0<x do
	x:=x-5
```
$$
\begin{align*}
&\langle x\ := 8; s_{0}\rangle,\  
\langle while\ (0<x)\ do \ (x:=x-5), s_{0}\rangle \\
\implies &
\langle while\ (0<x)\ do \ (x:=x-5), s_{0}[x \rightarrow \mathcal{A}[[8]]s_{0}]\rangle\  \\
\implies &
\langle if\ (0<x)\ then ((x:=x-5); while\ (0<x)\ do\ (x:=x-5))\ else\ skip, s_{0}[x\rightarrow \mathcal{A}[[8-5]]s_{0}]\rangle\\\\
\implies &
\langle while\ (0<x)\ do \ (x:=x-5), s_{0}[x \rightarrow \mathcal{N}[[3]]s_{0}]\rangle\  \\
\implies &
\langle if\ (0<x)\ then ((x:=x-5); while\ (0<x)\ do\ (x:=x-5))\ else\ skip, s_{0}[x\rightarrow \mathcal{A}[[3-5]]s_{0}]\rangle\\\\
\implies &
\langle while\ (0<x)\ do \ (x:=x-5), s_{0}[x \rightarrow \mathcal{N}[[-2]]s_{0}]\rangle\  \\
\implies &
\langle if\ (0<x)\ then ((x:=x-5); while\ (0<x)\ do\ (x:=x-5))\ else\ skip, s_{0}[x\rightarrow \mathcal{N}[[-2]]s_{0}]\rangle\\
\implies &
\langle skip, s_{0}[x \rightarrow \mathcal{N}[[-2]]s_{0}]\rangle\\
\implies &
s_{0}[x \rightarrow \mathcal{N}[[-2]]s_{0}]
\end{align*}
$$
