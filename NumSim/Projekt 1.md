
# Raketens bana
$$
m(t)\boldsymbol{\vec{a}}(t) 
= 
\boldsymbol{\vec{F}} 
+ 
m'(t)\boldsymbol{\vec{u}}(t)
$$
$m(t)\boldsymbol{\vec{a}}(t)$ beskriver *accelerationskraften på raketen*
$\boldsymbol{\vec{F}}$ beskriver *summan av externa krafter* (gravitation och luftmotstånd)
$m'(t)\boldsymbol{\vec{u}}(t)$ beskriver *kraften raketen utsätts för av expulsion av bränsle*

$$
\boldsymbol{\vec{F}} = m(t)\boldsymbol{\vec{g}} - c\ ||\vec{v}(t)||\ \vec{v}(t)
$$
Raketens egna massa är konstant på 4 kg
Ursprunglig massa bränsle är 4 kg
Raketens totala massa är en funktion av tiden:
$$
m(t) = \begin{cases}
8 - 0.4t & t \leq 10 \\
4 & t > 10
\end{cases}
$$

Bränslet skjuts med konstant hastighet $k_{m}$, raketens *hastighetsvektor* är alltså:
$$
\boldsymbol{\vec{u}}(t) = 
\begin{pmatrix}u_{x}(t)\\u_{y}(t)\end{pmatrix} =
\begin{pmatrix}k_{m}cos(\theta(t))\\k_{m}sin(\theta(t))\end{pmatrix}
$$
## Konstanter
$$
\begin{cases}
t = [0, 10] \\
k_{m} = 700 m/s \\
c = 0.05 kg/m \\
\boldsymbol{\vec{g}} = \begin{pmatrix}0\\-9.82\end{pmatrix}\\
mål = (x, y) = (80, 60)
\end{cases}
$$
## Starttillstånd
$$
\begin{cases}
m(0) = 8 \\
\vec{v}(0) = (0, 0) \\
pos = (0,0) \\
\theta= \pi / 2
\end{cases}
$$
## Uppgiftsbeskrivning
- Identifiera en lämplig funktion för vinkeln $\theta(t)$ sådan att raketen träffar målet.
- Raketen *måste* nå en höjd på *minst 20 meter* innan vinkeln får justeras.

## Tillvägagångssätt
- Vi identifierar $m'(t)$ från definitionen av $m(t)$:
$$
m'(t) = \begin{cases}
0.4 & t \leq 10 \\
0 & t > 10
\end{cases}
$$
- Derivatan av positionsvektorn = hastighet $\vec{v}(t)$
- Derivatan av hastighetsvektorn = acceleration $\vec{a}(t)$
- Vi bryter ut accelerationsvektorn
$$
\boldsymbol{\vec{a}}(t) 
= 
\boldsymbol{\vec{F}}/m(t) 
+ 
\frac{m'(t)\boldsymbol{\vec{u}}(t)}{m(t)}
$$
- Byter notation till v'(t)
$$
\vec{v}\ '(t) 
= 
\boldsymbol{\vec{F}}/m(t) 
+ 
\frac{m'(t)\boldsymbol{\vec{u}}(t)}{m(t)}
$$
- Vi förlänger $\boldsymbol{\vec{F}}$ 
$$
\vec{v}\ '(t) 
= 
\frac{m(t)\boldsymbol{\vec{g}} - c\ ||\vec{v}(t)||\ \vec{v}(t)}{m(t)}
+ 
\frac{m'(t)\boldsymbol{\vec{u}}(t)}{m(t)}
$$
$$
\vec{v}\ '(t) 
= 
\boldsymbol{\vec{g}} - \frac{c\ ||\vec{v}(t)||\ \vec{v}(t)}{m(t)}
+ 
\frac{m'(t)\boldsymbol{\vec{u}}(t)}{m(t)}
$$
$$
\vec{pos}\ ''(t) 
= 
\boldsymbol{\vec{g}} - \frac{c\ ||\vec{v}(t)||\ }{m(t)} \vec{v}(t)
+ 
\frac{m'(t)}{m(t)}\boldsymbol{\vec{u}}(t)

$$
$$
\vec{pos}\ ''(t) 
= 
\boldsymbol{\vec{g}} - \frac{c\ ||\vec{pos}'(t)||\ }{m(t)} \vec{pos}'(t)
+ 
\frac{m'(t)}{m(t)}\boldsymbol{\vec{u}}(t)

$$

$$
\vec{pos}(0) = \begin{pmatrix}0\\0\end{pmatrix}\ \ \ \
\vec{pos}\ '(0) = \begin{pmatrix}0\\0\end{pmatrix}\\ \\
$$
$$
\vec{pos}\ ''(0) = \begin{pmatrix}0\\-9.82\end{pmatrix} - \frac{0.05*0}{8}\begin{pmatrix}0\\0\end{pmatrix} +
\frac{4}{8} \begin{pmatrix}700 * cos(\pi/2)\\700 * sin(\pi/2)\end{pmatrix}
$$
$$
\vec{pos}\ ''(0) = \begin{pmatrix}0\\-9.82\end{pmatrix} + \begin{pmatrix}350 * cos(\pi/2)\\350 * sin(\pi/2)\end{pmatrix}
$$
$$
\vec{pos}\ ''(0) = \begin{pmatrix} 0 \\ 340.18 \end{pmatrix}
$$
$$
\vec{pos}(0) = \begin{pmatrix}0\\0\end{pmatrix}\ \ \ \
\vec{pos}\ '(0) = \begin{pmatrix}0\\0\end{pmatrix}\ \ \ \ \vec{pos}\ ''(0) = \begin{pmatrix} 0 \\ 340.18 \end{pmatrix}
$$

```python
g = [0, -9.82] # m/s/s
tspan = np.arange(0, 10, 0.1)
km = 700 # m/s
c = 0.05 # kg/m
target = [80, 60]

def m_func(t):
	return 8 - 0.4t if t <= 10 else 4

def m_prime(t):
	return 0.4 if t <= 10 else 0
	
def theta_func(t):
	return math.pi/2
	
def u_func(t):
	return [km * math.cos(t), km * math.sin(t)]

def ode_solver(t, posvec):
	pos_deriv = np.zeros(2)
	pos_deriv[0] = posvec[1]
	pos_deriv[1] = g - ((np.norm(posvec[1]) * c / m_func(t)) * posvec[0]) + m_prime(t) / m_func(t) * u_func(t)
	

```