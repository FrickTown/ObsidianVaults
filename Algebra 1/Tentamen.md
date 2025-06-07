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
Om x i fråga är ett *primtal* så är *alla* tal upp till *x-1*  co-prima.

Om vi har *flera av samma* primfaktor:
<span style="display: flex; justify-content: center;"><img src="Pasted image 20250607144046.png"</img></span>
Exempelvis $\phi(27) = \phi(3^{3}) = 3^{3-1}(3-1) = 9*2 = 18$

Om vi har *flera olika* primfaktorer kan vi lösa med denna formel
Om samma primfaktor uppstår fler än en gång så åsidosätter vi den för formeln och multiplicerar in den efter formeln.
<span style="display: flex; justify-content: center;"><img src="Pasted image 20250607145248.png"</img></span>
$$
\begin{cases}
x = 280 \\
primfaktorer\ till\ 280 = 2 * 2 * 2 * 5 * 7 \\
\phi(280) = 2 * 2 * 2 * 5 * 7 * \frac{2-1}{2} * \frac{5-1}{5} * \frac{7-1}{7} \\
\phi(280) = 2*2*1*4*7 = 96
\end{cases}
$$
## Eulers sats

## Kinesiska restsatsen
Givet ett system av kongruenser, hitta talet som ger rätt rest för alla kongruenser
Alltså
$$
\begin{cases}
A: x \equiv 2\ (mod\ 4) \\
B: x \equiv 4\ (mod\ 5) \\
C: x \equiv 6\ (mod\ 13) \\
\end{cases}
$$
Vilket tal x passar in i detta system?

1. Hitta ett x som stämmer in på $2 (mod 4)$
   $x = 2 + 4n$ = 2, 6, 10, 14, 18
2. Hitta ett x från ovanstående som stämmer in på $4(mod5)$
   $x = 4 + 5n$ = 4, 9, *14*, 19
   14 löser A och B.
3. Om vi ska leta tal för C, börjar vi med vår bästa lösning hittills: *14*
   Eftersom alla tal vi testar måste fortsatt vara delbar med både 4 och 5 hittar vi minsta gemensamma multipeln: MGD(4, 5) = 20. Detta använder vi som intervall.
4. Vi letar nu efter ett x enligt $x = 14 + 20n$ som stämmer in på $6(mod\ 13)$.
   Vi kan ta intervallet mod 13 för att se hur mönstret kommer se ut för
   $14 + 20n\ (mod\ 13)$ : $20 (mod 13) = 7$
   $14 (mod 13) = 1$
   len(\[ 1, *8, 2, 9, 3, 10, 4, 11, 5, 12, 6*]) - 1 = 10
   $14 + 20*10=214$  
   Alla svar: $214+ (4*5*13)n$
5. 
   