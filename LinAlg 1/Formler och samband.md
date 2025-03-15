# Kapitel 1: *Planet* $\mathbb{R}^2$
### Magnitud
$$\vec{v} = 
\begin{pmatrix} a\\ b\end{pmatrix}
$$
$$||v|| = \sqrt{a^{2}+ b^2}$$

### Skalärprodukt
#Skalärprodukten definieras som *a*s projektion på *b* multiplicerad med längden av *b*. 
$$a \cdot b=||a||*||b||*cos\theta$$
Där theta är vinkeln mellan a och b.
Skalärprodukten kan också beräknas
$$
a\cdot b =\begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix}\cdot\begin{pmatrix}b1\\b2\\b3\end{pmatrix} = 
a_1b_1+a_2b_2+a_3b_3
$$
### Def: R(-)
Rotation med $$\frac{\pi}{2}$$ 
### #Ortogonal projektion
En vektor *w* pekar åt ett icke-ortogonalt håll från *v*. Hur finner vi en vektor *a* som är parallell med vektorn *v*, som vid sitt apex kan peka en ortogonal vektor mot apex av *w*?
Den **ortogonala** projektionen av w på v är:
$$
proj_{\vec{v}}\vec{w} = \frac{\vec{v}\cdot\vec{w}}{||\vec{v}||^2}\vec{v}
$$
<span style="display: flex; justify-content: center;"><img src="Pasted image 20250204201408.png"</img></span>

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
<span style="display: flex; justify-content: center;"><img src="Pasted image 20250204212743.png"</img></span>
k = 2 men 2k = 3 går inte ihop. Därav är ***inte*** de två vektorerna parallella.

### Avstånd mellan två punkter i 3D
Avståndet är definierat som längden av vektorn $\vec{PQ}$
$$
d(P,Q) = ||\vec{PQ}|| = \sqrt{(x_{2}- x_{1})^2+(y_{2}- y_{1})^2+(z_{2}-z_{1})^2}
$$
### Avstånd mellan punkt till plan
Avstånd mellan punkten $(x_{0}, y_{0}, z_{0})$ till planet $a_{x}+b_{y}+c_{z}=d$
kan bestämmas med formeln
$$
\frac{|d-ax_{0}-by_{0}-cz_{0}|}{\sqrt{a^2+b^2+c^2}}
$$
 ### Skalärprodukt
$$
\vec{v}\cdot\vec{w} := ||\vec{v}||\ ||\vec{w}|| \cos(\theta) = v_1w_1+v_2w_2+v_3w_3
$$
Skalärprodukten av två vektorer pekandes ifrån en punkt är större än 0 om vinkeln är spetsig, mindre än 0 om vinkeln är trubbig. *0 om dessa är parallella.*
### Skärningspunkt av linje i plan
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

### Punkt på ett plan närmst en punkt
Låt $\pi$ definiera ett plan, och Q definiera en punkt:
$\pi = x+y-z=5$
$Q = (1,1,1)$
Då är planets #normalvektor (koefficienterna för x, y och z): $\begin{pmatrix}1\\1\\-1\end{pmatrix}$
Vi kan definiera en linje som går igenom punkt Q som skär planet genom att gå från punkt Q och följa planets normalvektor:
$l = \begin{pmatrix}1\\1\\1\end{pmatrix} + t \begin{pmatrix}1\\1\\-1\end{pmatrix}$

Vi löser skärningspunkten genom att sätta in linjens ekvation i planet:
$P = (1+t)+(1+t)-(1-t) = 1+3t = 5 \implies t=\frac{4}{3}$ 

VI har ett värde på $t$ att sätta in i linjen $l$:
$Svar: (x,y,z)=(\frac{7}3, \frac{7}3, -\frac{1}3)$

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
	\vec{AB} \cdot \vec{L} = -1-19t-9s = 0\\
	\vec{AB} \cdot \vec{K} = 9t+5s = 0
\end{cases}
$$
Nu kan vi lösa ut $t$ och $s$:
$$
\begin{split}
9t + 5s = 0 \implies s = \frac{-9}5t\\
-1-19t-9s =0 \implies 19t+9(\frac{-9}5t)=-1\\
\implies 19t+\frac{-81}{5}t=-1\implies 95t-81t = -5\\
\implies14t = -5 \implies t = \frac{-5}{14}
\end{split}
$$
$s$ kan återfås genom att substituera $t$ med $\frac{-5}{14}$
*Punkten på $L$ närmast $K$ kan nu beräknas genom att substituera in $t$ i ekvationen en generell punkt $A$ på $L$:*

### Vektorprodukten
Vektorprodukten mellan $\vec{v}$ och $\vec{w}$ noteras $\vec{v} \times \vec{w}$ och uppfyller:
- $||\vec{v} \times \vec{w}|| = ||\vec{v}||\ ||\vec{w}||\sin{\theta}$ (Magnituden av vektorprodukten är #skalärprodukten, och därmed även *arean* *på* *parallellogrammen* som $\vec{v}$ och $\vec{w}$  definierar.
- Riktningen av $\vec{v} \times \vec{w}$ är ortogonal till både $\vec{v}\ och\ \vec{w}$
- Om $\vec{v}\ och\ \vec{w}$ *ej* är parallella så pekar $\vec{v} \times \vec{w}$ i en riktning *ortogonal* mot $\vec{v}\ och\ \vec{w}$ som en plankonstellation.
Om $\vec{v}$ och $\vec{w}$ *är* parallella så är $\vec{v} \times \vec{w} = \begin{pmatrix}0\\0\\0\end{pmatrix}$ 
Vektorprodukten är definierad som följande:
<span style="display: flex; width:100%; border-bottom: 3px solid yellow; justify-content:center;"></span>
$$
\begin{pmatrix}v1\\v2\\v3\end{pmatrix}
\times
\begin{pmatrix}w1 \\ w2 \\ w3\end{pmatrix}
=
\begin{pmatrix}v_2w_3-v_3w_2\\v_3w_1-v_1w_3\\v_1w_2-v_2w_1\end{pmatrix}
$$
<span style="display: flex; width:100%; border-bottom: 3px solid yellow; justify-content:center;"></span>
Mnemonic: Skifta första kolumnen i vänsterspalten -1 steg, andra kolumnen +1 steg. Matcha i högerspalten med inversen.
Övriga räkneregler för vektorprodukten:
<span style="display: flex; justify-content: center;"><img width="350px" src="Pasted image 20250214124855.png"</img></span>
### Volymen för en parallellepiped
En parallellepiped är ett parallellogram med djup.
<span style="display: flex; justify-content: center;"><img src="Pasted image 20250215172456.png"</img></span>
Volymen för en sådan beräknas som följande:
$$
Volym= |(\vec{u}\times\vec{v})\ \bullet\ \vec{w}|
$$
 Absolutbeloppet av #skalärprodukten av #vektorprodukten $\vec{u}\times\vec{v}$ och $\vec{w}$.
 Detta eftersom att magnituden av skalärprodukten $\vec{u}\times\vec{v}$ motsvarar arean på parallellogrammen som $\vec{u}$ och $\vec{v}$ utgör.
 Vi kan tänka oss att höjden på parallellogrammen är
 $$h = |\cos(\alpha)||\vec{w}|||$$ och därmed, bas gånger höjd blir
 $$
 Volym = \cos(a)\ ||\vec{w}||\ ||\vec{u}\times\vec{v}||
$$
eller 
$$
Volym= |(\vec{u}\times\vec{v})\ \bullet\ \vec{w}|
$$

Om en *parallellepiped har en volym på 0* så måste *någon* av vektorerna vara *parallella* med varandra. 

# Kapitel 3: **Linjära** ekvationssystem 
### Linjär ekvation: form
En linjär ekvation skrivs på formen 
$$
a_1x_1+a_2x_2+...+a_nx_{n}=b
$$
### Grundläggande operationer
Nedanstående två ekvationer med samma obekanta $x,y$ är två linjer i planet.
$$\begin{cases}x+3y=1\\2x-y=3 
 \end{cases}
 $$
 Strategin är att skriva om ekvationssystemet till ett enklare system.
$$
\begin{cases}a_1x+b_{1y}=c_1 \\
a_2x+b_2y=c_2 
\end{cases}
$$
Nedanstående *operationer* kommer tillämpas för att uppnå det:

**1.** ($\lambda$)$\uparrow$  Ta ekvationen, multiplicera den med en konstant $\lambda$ . Addera resultatet i ovanstående ekvation.

$$
\begin{cases}
a_1x+b_1y=c_{1}  \\
a_{2}x+ b_{2}y= c_2 (\lambda)\uparrow
\end{cases}
\implies
\begin{cases}
(a_{1}+ \lambda a_{2}))x+(b_1+\lambda b_{2)y} = c_{1}+\lambda c2\\
a_{2}x + b_{2}y = c_2& 
\end{cases} 
$$

 *2.* ($\lambda$) Multiplicera ekvationen med konstanten $\lambda$.

*3.* $\frac{\nwarrow}{\swarrow}$ Byt plats på ekvationerna

### Totalmatris
En totalmatris för ett linjärt ekvationssystem delar upp alla koefficienter på vänsterled i en matris, och kända värden på högerled i en annan, och sedan sammanfogar dessa:
$$
\begin{cases}
x_{1}+2x_{2}-x_{3}+ x_{4}= 1 \\
2x_{1}- x_{2}+ x_{3}-x_{4}= 3 \\
x_{1}-3x_{2}+2x_{3}-2x_{4}=4
\end{cases}
\implies
\begin{pmatrix}
1 & 2 & -1 & \ \ \ 1 |\ 1\\
2 & -1 & 1 & -1 |\ 3\\
1 & -1 & 2 & -2|\ 4\end{pmatrix}
$$
### Gauss-Jordan eliminering
1. Hitta totalmatrisen
2. Använd operationer för att uppnå trappstegsmatris
3. Gör matrisen radkanonisk
4. Färdig

# Kapitel 4: *Matriser*
### Matrisaddition
Precis som man hade tänkt sig
### Matrismultiplikation
För matrismultiplikation *krävs* att **antalet kolumner i A matchar antalet rader i B**.
Ta första *raden* av A och multiplicera varje index med respektive index i första *kolumnen* av B. Addera dessa för att få index (0, 0). För att få index (1, 0) så tar du samma rad från A, men nästa kolumn i B. Detta repeteras sedan för resten.
$$
\begin{pmatrix}a1\\b\\c\end{pmatrix}
$$

### Matrisinvers
#### Definition:
Låt $I$ vara en enhetsmatris.
$$
\begin{pmatrix} 
& 1& 0& 0& \\ & 0& 1& 0\\ & 0&  0& 1\end{pmatrix}
$$
Om det för en $(n \times n)$ matris A finns en $(n\times n)$ matris C så att:
	$AC = CA = I$
Så är C *entydigt* bestämt av A och kallas C = $A^{-1}$.
*A måste ha rang n* för att vara inverterbar.
#### Beräkning:
Om vi söker inversen av A, $A^{-1}$, så innebär det att det måste finnas en lösning C så att
	$AC = CA = I$ 
$I$ motsvarar alltid en enhetsmatris i samma rang som A. 
Låt
$$
A=\begin{pmatrix} 
& 1& 1& 2& \\ & 1& 1& 1\\ & 1&  2& 3\end{pmatrix}
\ I=\begin{pmatrix} 
& 1& 0& 0& \\ & 0& 1& 0\\ & 0&  0& 1\end{pmatrix}
$$
Kombinera dessa till en Gauss-Jordan-kompatibel totalmatris och lös den. Resultatet $C = A^{-1}$ kommer återfinnas i högerledet, medans *vänsterledet kommer vara en enhetsmatris*
$$
\begin{pmatrix} 
  1& 1& 2\ |\ 1& 0& 0
\\1& 1& 1\ |\ 1& 1& 0
\\1& 2& 3\ |\ 1& 0& 1
\end{pmatrix}
\implies
\begin{pmatrix} 
  1& 0& 0\ |& 1& 1& -1
\\0& 1& 0\ |& -2& 1& 1
\\0& 0& 1\ |& 1& -1& 0
\end{pmatrix}
$$
Alltså är A inverterbar med inversen:
$$
A^{-1} = \begin{pmatrix} 
  1& 1& -1
\\-2& 1& 1
\\1& -1& 0
\end{pmatrix}
$$
### Räkneregler
<span style="display: flex; justify-content: center; "><img style="width: 100%;" src="Pasted image 20250315170816.png"</img></span>
# Kapitel 5: *Generellt* $\mathbb{R}^n$ och baser
### Normera en vektor
Att normera en vektor innebär att bevara riktningen men göra längden till 1.
$$
norm(\vec{v}) = \frac{1}{||\vec{v}||}\vec{v}
$$
### Span (Linjärt hölje)
*Spannet* av ett set med vektorer definieras som mängden vektorer som är **linjärkombinationer** av dessa.
En linjärkombination innebär att ett set med konstanter $c_{1}, c_{2}, c_{3} ..., c_{n}$,  kombineras med ett set av vektorer $v_{1},v_{2},v_{3},\cdots,v_{n}$, för att bilda en vektor $c_{1}\vec{v}_{1}+c_{2}\vec{v}_{2} + \cdots + c_{n}\vec{v}_{n}$ . 

Spannet av ett set vektorer avgör alltså vilka delar av rummet vi kan nå genom att kombinera dessa. *Om två eller flera av vektorerna är parallella begränsas vi till ett snitt av rummet.* Alltså i 2D kan spannet vara en linje, eller hela $\mathbb{R}^2$. I 3D kan spannet vara en linje, om alla tre vektorer är parallella, ett plan om två vektorer är parallella, eller hela $\mathbb{R}^3$ 

Vi kan bestämma spannet givet ett set med vektorer genom att försöka hitta en generell lösning för en vektor som är en linjärkombination av vektorerna.

Givet $\vec{u} = \begin{pmatrix}1\\2\\3\end{pmatrix}, \vec{v} = \begin{pmatrix}3\\2\\1\end{pmatrix}, \vec{w} = \begin{pmatrix}0\\0\\0\end{pmatrix}$

Så kan vi hitta spannet $Span\{\vec{u},\vec{v},\vec{w}\}$ genom att skapa en totalmatris:
$$
\begin{pmatrix}
1 & 3 & 0 & | & b_{1}\\
2 & 3 & 0 & | & b_{2}\\
3 & 1 & 0 & | & b_{3}
\end{pmatrix}
$$
Och lösa denna med Gauss-Jordan elimination.
Spannet är hela $\mathbb{R}^n$ om vi kan sätta vektorerna av grad i en ($n \times k$) totalmatris, och ***rangen*** på denna är n. Detta eftersom att oändliga svar på vektorn V = $\begin{pmatrix}b_1\\b_2\\b_3\end{pmatrix}$ kan ges och ingen är beroende av de andra.
Om vi får en 0-rad så återfås en ekvation, och vektorn V ligger endast i spannet om ekvationen gäller.

### Linjärt oberoende
Två vektorer $\vec{v}$ och $\vec{w}$ är parallella om  några skalärer $c1, c2$ finns så att $c_{1}\vec{v}+c_{2}\vec{w}=\vec{0}$.
Ett set vektorer anses *linjärt oberoende* (icke-parallella i n-dimensioner) om den enda linjära kombinationen som resulterar i 0 som kan göras med dessa är om alla skalärer är 0.

Ledande element i varje rad => Hela R^n  (ej om 0-rad)

### Bas och koordinater i en bas
#### Definition:
En ordnad uppsättning vektorer kallas en **bas** om *spannet* är hela rummet, och alla vektorer är linjärt oberoende.
En bas för $\mathbb{R}^n$ består av n vektorer.
*En godtycklig bas måste ha rang $k$, den måste alltså vara kvadratisk.*

För en bas $\underline{\textbf{V}} = (\vec{v}_1,\vec{v}_2)$ för $\mathbb{R}^2$ och en vektor $\in \mathbb{R}^2$ där
$$
\vec{u} = t\vec{v}_{1}+s\vec{v}_{2}
$$
kallar vi
$$
[\vec{u}]_{\underline{\textbf{V}}} = \begin{pmatrix}t\\s\end{pmatrix}
$$
koordinaterna av $\vec{u}$ i basen $\underline{\textbf{V}}$.

De vanliga koordinaterna för ett rum är dess *enhetsvektorer*. För $\mathbb{R}^2$ är dessa alltså $\begin{pmatrix} \begin{pmatrix}1\\0\end{pmatrix},\begin{pmatrix}0\\1\end{pmatrix}  \end{pmatrix}$ 
#### Exempel
Låt
$$
\underline{\textbf{V}} = (\vec{v}_{1},\vec{v}_{2})
\ \ \ \vec{v}_{1}=\begin{pmatrix}2\\1\end{pmatrix},
\vec{v}_{2}=\begin{pmatrix}-2\\1\end{pmatrix}
$$
Om vill hitta koordinaterna för $\begin{pmatrix}0\\6\end{pmatrix}$ i basen $\underline{\textbf{V}}$ måste vi hitta $t, s$ *så att* $t\begin{pmatrix}2\\1\end{pmatrix} + s\begin{pmatrix}-2\\1\end{pmatrix} = \begin{pmatrix}0\\6\end{pmatrix}$

Vi ställer upp i totalmatris
$$
\begin{pmatrix}
2 & -2 & | & 0\\
1 & 1 & | & 6
\end{pmatrix}
$$
Lös till radkanonisk:
$$
\begin{pmatrix}
1 & 0 & | & 3\\
0 & 1 & | & 3
\end{pmatrix}
$$
Alltså är $(t,s) = (3,3)$ 

# Kapitel 6: *Linjära* Avbildningar
### Avbildningar
Avbildning är synonymt med *funktion*.
För $T : \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$ används notationen:
$$
\vec{y} = T(\vec{x})
$$
Och vi säger "$\vec{y}$ 'r *bilden* av $\vec{x}$ under $T$".
### Matrisavbildningar
Om produkten av en funktion är en matris kallas det en *matrisavbildning*.

### Standardmatriser
*Standardmatrisen* för en avbildning $T$ betecknas $[T]$. Om vi har en linjär avbildning $T$ som uppfyller
$$
T\begin{pmatrix}1\\1\end{pmatrix} = \begin{pmatrix}1\\1\\1\end{pmatrix}\ \ och\ \
T \begin{pmatrix}1\\2\end{pmatrix}=\begin{pmatrix}2\\2\\3\end{pmatrix}
$$
Så återfinns $[T]$
$$
[T] = \begin{pmatrix}1 & 2\\1 & 2\\1 & 3\end{pmatrix} \begin{pmatrix}1 & 1\\1 & 2\end{pmatrix}
$$
### Linjära avbildningar
#### Definition
En avbildning $T : \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$ anses *linjär* om den uppfyller att:
- $T(\vec{v} + \vec{w}) = T(\vec{v}) + T(\vec{w})$
- $T(k\vec{v}) = kT(\vec{v})$
En godtycklig linjär avbildning *är en matrisavbildning*
