## Funktioner
### Injektiv
"No two inputs generate the same output"
Linjära funktioner, såsom $2x + 3$ eller polynomfunktioner såsom $x^2$ 
### Surjektiv
"All outputs have an input"
#### Surjektiv
$f: \mathbb{Z} \rightarrow \mathbb{Z}$
$f(x) = x^2$
#### Inte surjektiv
$f: \mathbb{Z} \rightarrow \mathbb{Z}$
$f(x) = \pm \sqrt{x-1}$
### Bijektiv

### Bijektion mellan två domäner
<span style="display: flex; justify-content: center;"><img src="Pasted image 20250607141522.png"</img></span>
a) Vi använder linjär interpolation
$f: [0, 1] \rightarrow [2, 7]$ 
$f(x) = 2 + x * (7 - 2)$
$f(0) = 2 + 0 * (7 - 2) = 2 + 0 = 2$
$f(1) = 2 + 0 * (7-2) = 2 + 5 = 7$
$f^{-1}: [2,7] \rightarrow [0, 1]$
$f(y) = \frac{y-2}{7-2}$
$f(2) = \frac{2-2}{7-2} = 0$
$f(7) = \frac{7-2}{7-2} = 1$

b)


## Diofantiska ekvationer

## Eulers phi-funktion
$\phi(x)$ = Antalet tal som är relativt prima till x från 1 till x-1
Hitta primfaktorer (om möjligt) till x, sen identifiera vilka tal från 1 till x-1 som inte delar någon av dessa primfaktorer.
$$
\begin{cases}
x = 15 \\
primfaktorer\ till\ 15 = 3*5 \\
1, 2, 4, 7, 8, 11, 13, 14 \\
Svar: \phi(15) = 8 
\end{cases}
$$
Om x i fråga är ett *primtal* så är *alla* tal upp till *x-1*  co-prima
<span style="display: flex; justify-content: center;"><img src="Pasted image 20250607144046.png"</img></span>
Exempelvis $\phi(27) = \phi(3^{3}) = 3^{3-1}(3-1) = 9*2 = 18$
Löses med 