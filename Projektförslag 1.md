# **Projektförslag för [M6] Pythonprojekt**
## Jakob Frick & Frey Tryggvarson
#### 2024-10-17
## Vår idé
Vår projektidé är en sinusvåg-visualiserare representerad med textsymboler i kommandotolken. Med hjälp av tangentbordet skall man kunna ändra på variablerna som avgör sinusvågens amplitud och våglängd "on the fly", alltså utan att starta om applikationen. Detta i syftet att bygga intuition för hur en sinusfunktion beror på sin koefficient, parameter och eventuella konstanter.

Trigonometri är en av matematikens mer visualiserbara grenar, och att bygga egen intuition för anatomin av en sinusvåg kan vara till stor hjälp inom alla områden som förlitar sig på dem. Optik, akustik, kvantmeknik, och övrig fysik som är grundat i harmonisk svängrörelse. I övrigt är interaktiv matematik väldigt underhållande att leka med, och även de som inte drar *nytta* av att studera sinusvågen kan ha kul med att fippla med värden och se hur vågen ändras.

## Systemets delar



### Kurvanpassning
Kurvan för en matematisk funktion i ett koordinatsystem har oändlig upplösning. Detta skiljer sig markant från skärmar på datorer, som har en ytterst ändlig upplösning. Det innebär att vi måste bestämma vilka "rutor" i kommandotolken som skall visa en symbol, och vilka som inte bör det, för att närmst representera kurvan. Det leder vidare in på ämnet upplösning.

### Upplösning
Kommandotolken har en satt upplösning, men som kan ändras i inställningarna för 