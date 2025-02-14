# Kapitel 1: *Planet* $\mathbb{R}^2$
### Magnitud
$$\vec{v} = 
\begin{pmatrix} a\\ b\end{pmatrix}
$$
$$||v|| = \sqrt{a^{2}+ b^2}$$

### Skalärprodukt
*a*s projektion på *b* multiplicerad med längden av *b*. 
$$a \cdot b=||a||*||b||*cos\theta$$
Där theta är vinkeln mellan a och b.
### Def: R(-)
Rotation med $$\frac{\pi}{2}$$ 
### #Ortogonal projektion
En vektor *w* pekar åt ett icke-ortogonalt håll från *v*. Hur finner vi en vektor *a* som är parallell med vektorn *v*, som vid sitt apex kan peka en ortogonal vektor mot apex av *w*?
Den **ortogonala** projektionen av w på v är:
$$
proj_{\vec{v}}\vec{w} = \frac{\vec{v}\cdot\vec{w}}{||\vec{v}||^2}\vec{v}
$$
![[Pasted image 20250204201408.png]]

### Normalekvation för en #linje: Mellan två punkter
Låt P och Q vara punkter (P<sub>x</sub>, P<sub>y</sub>) och (Q<sub>x</sub>, Q<sub>y</sub>)
För att etablera en linje på #normalekvation på formen:
$$
Ax+By+C =0
$$
mellan dessa:
$$
\begin{split}
A = Q_{y}-P_{y}\\
B = P_{x}-Q_{x}\\
C=P_{y}\times(Q_x-P_{x})-P_{x}\times(Q_y-P_{y)}
\end{split}
$$
$$

$$
# Kapitel 2: *Rummet* $\mathbb{R}^3$
### Parallellitet
$$\vec{v}\ är\ parallell\ med\ \vec{w}\ omm\  \vec{v} = k\vec{w}$$
Alltså om *w* är en omskalning av *v*.
Nedan följer ett lätt sätt att identifiera huruvida två vektorer är parallella.
![[Pasted image 20250204212743.png]]
k = 2 men 2k = 3 går inte ihop. Därav är ***inte*** de två vektorerna parallella.

### Avstånd mellan två punkter i 3D
Avståndet är definierat som längden av vektorn $\vec{PQ}$
$$
d(P,Q) = ||\vec{PQ}|| = \sqrt{(x_{2}- x_{1})^2+(y_{2}- y_{1})^2+(z_{2}-z_{1})^2}
$$
### Skalärprodukt
$$
\vec{v}\cdot\vec{w} := ||\vec{v}||\ ||\vec{w}|| \cos(\theta) = v_1w_1+v_2w_2+v_3w_3
$$
### <span style="border: 2px solid violet">Skärningspunkt av linje i plan</span>
$$Linjen\ l:(x,y,z) = (1+2t,t,1),t\in\mathbb{R}$$
$$Planet\ \pi:2x+3y - 22z = 1$$
Vi sätter in beskrivningen av punkterna på linjen i ekvationen för planet:
$$
\begin{split}
2(1+2t)+3(t)-22(1)=1\\
2+4t+3t-22 = 1 \implies t=3\\
\end{split}
$$
Detta nya t sätter vi in i linjen:
$$
Skärningspunkt\ =(x,y,z) = (1+(2*3), 3, 1) = (7,3,1)
$$

### Punkt på en linje närmst en annan linje
Vi har två linjer på *parameterform*:
$L = \begin{pmatrix} 0\\ 1\\ -1\end{pmatrix} + t\begin{pmatrix} 1\\ 3\\ 3\end{pmatrix}$
$K = \begin{pmatrix} -1\\ 1\\ -1\end{pmatrix} + s\begin{pmatrix} 0\\ -1\\ -2\end{pmatrix}$

Vi kan säga att en *generell* *punkt* på respektive linje definieras:
$L: A= (t, 1+3t, -1+3t)$
$K: B= (-1, 1-s, -1-2s)$

Nu när vi kan säga vad en generell punkt är, så kan vi också säga vad *vektorn* är mellan två generella punkter A och B genom att subtrahera B med A.
$\vec{AB} = \begin{pmatrix}(-1)-(t)\\(1 - s)-(1+3t)\\(-1-2s) - (-1 + 3t)\end{pmatrix}$ 
Vilket förenklas som
$\vec{AB} = \begin{pmatrix}-1-t\\-s-3t\\2s-3t\end{pmatrix}$ 

Med hjälp av *riktningsvektorerna* för $L$ och $K$ så kan vi utveckla ett ekvationsystem för att lösa ut värden på $t$ och $s$. Detta gör vi genom att ta skalärprodukten av $\vec{AB}$ och respektive riktningsvektor
$$
\begin{cases}
	\vec{AB} \cdot \vec{L} = 1(-1-t)+3(-s-3t)+3(-2s-3t)\\
	\vec{AB} \cdot \vec{K} = 0(-1-t)-1(-s-3t)-2(-2s-3t)
\end{cases}
$$
Vilket förenklas till:
$$
\begin{cases}
	\vec{AB} \cdot \vec{L} = -1-19t-9s\\
	\vec{AB} \cdot \vec{K} = 0(-1-t)-1(-s-3t)-2(-2s-3t)
\end{cases}
$$
