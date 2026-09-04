1. *Förklara begreppet Maskinepsilon och vad det har för betydelse för talrepresentationen i datorn.*
Maskinepsilon är det minsta möjliga steget datorn kan ta längsmed den reella talinjen efter talet 1. Den avgör noggrannhet i flyttalrepresentationen i en dator.
2. *När man löser ODEr numerisk så approximerar man derivatorna med differenskvoter. I nedanstående figur har man använt framåtdifferensen för att approximera en derivata*
$$
f'(x) \approx f'(x) = \frac{f(x_{i+1})-f(x_{i})}{h}
$$
	*till en funktion och sedan plottat felet av derivatan, skillnaden mellan $\tilde{f}'(x) och f'(x)$ , som en funktion av steglängden $h = x_{i+1} − x_{i}$ 
	
![[Pasted image 20260902153345.png]]

*Förklara med ord varför felet beter som den gör i figuren för olika steglängder. Vilka konsekvenser och begränsningar ger det när man ska lösa en ODE numeriskt?*
Stora tal tenderar att vara mindre precisa i standard flyttalsrepresentation på datorer. Därför ser vi att felet minskar från höger till vänster, när vi rör oss mot ~-28 på x-axeln.
Felet är mer variabelt till vänster om ~-28 på grund av avrundningsfel. Talen börjar bli mindre med fler decimalplatser, och det är lätt att data går förlorad vid aritmetiska operationer.
Felet blir konstant till vänster om ~-53 på grund av maskinepsilon. Vi försöker nu ta sådana små steg att vi inte längre avancerar längsmed tallinjen, $1 + h_{\epsilon} = 1$. 

Vid numerisk lösning av ODEr så använder man sig av en steglängd, $h$, tillsammans med lutningen vid en känd punkt, för att estimera vart en efterträdande punkt skulle kunna ligga på funktionens kurva. En liten steglängd kommer ge mer precisa estimeringar. Att en dators flyttalsrepresentation har ett minsta delta, och att denna även blir mindre noggrann vid stora tal, kan leda till en oacceptabelt stor felmarginal när vi försöker estimera något med hög noggrannhet, exempelvis när vi försöker göra en komplex och precis fysiksimulation.

3. *Antag att vi vill simulera ett fysikaliskt fenomen med numeriska metoder, vilka olika felkällor kan påverka noggrannheten och tillförlitligheten i lösningen?*
- Mätfel vid insamling av data
- Dålig approximering av fenomenet (inte identifierat alla variabler)
- Diskretiseringsfel för stora tal
- Avrundningsfel för små tal