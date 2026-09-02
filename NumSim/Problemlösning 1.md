1. *Förklara begreppet Maskinepsilon och vad det har för betydelse för talrepresentationen i datorn.*
Maskinepsilon är det minsta möjliga steget datorn kan ta längsmed den rationella talinjen. Den avgör noggrannhet i talrepresentationen.
2. *När man löser ODEr numerisk så approximerar man derivatorna med differenskvoter. I nedanstående figur har man använt framåtdifferensen för att approximera en derivata*
$$
f'(x) \approx f'(x) = \frac{f(x_{i+1})-f(x_{i})}{h}
$$
	*till en funktion och sedan plottat felet av derivatan, skillnaden mellan $\tilde{f}'(x) och f'(x)$ , som en funktion av steglängden $h = x_{i+1} − x_{i}$ 
<span style="display: flex; justify-content: center;"><img style="width:75%" src="Pasted image 20260902153345.png"</img></span>
	Förklara med ord varför felet beter som den gör i figuren för olika steglängder. Vilka konsekvenser och begränsningar ger det när man ska lösa en ODE numeriskt?*
Felet är mer variabelt till vänster om -28 på grund av avrundningsfel.
Felet blir konstant till vänster om -52 på grund av maskinepsilon. 

3. *Antag att vi vill simulera ett fysikaliskt fenomen med numeriska metoder, vilka olika felkällor kan påverka noggrannheten och tillförlitligheten i lösningen?*
4. 