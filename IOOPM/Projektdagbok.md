# Torsdag 8 Januari 2025
*Tid: 60 minuter*
Jag finslipade gårdagens kod, och gjorde den mer generisk. En registrerad typ kan nu göras med upp till 6 pekare som ska frias. Denna gräns är lätt justera, med en enstaka rad eller två till med macrokod. 
# Onsdag 7 Januari 2025
*Tid: 240 minuter*
Jag kallade till nödmöte på kort varsel 
Jag bestämde mig för att ta itu med type registration och default destructors. Det tog en stund att reda ut macros (det är verkligen ett helt ytterligare språk att lära sig), men den slutgiltiga produkten blev väldigt bra och exakt enligt specifikationer. Det var en lärorik process och det roligaste jag haft med projektet hittills, då det utmanade mig mer än de tidigare bitarna.
# Måndag 5 Januari 2025
*Tid: 30 minuter*
Jag märkte lite brister i hash table integrationen som jag korrigerade. Nu är repot redo för större förändringar.
# Onsdag 31 December 2025
*Tid: 60 minuter*
Integrationen av ref counter i hash table var nu godtyckligt implementerad, så jag mergeade den.
# Lördag 27 December 2025
*Tid: 120 minuter*
Efter en välbehövlig julpaus satte jag mig ned för att reviewa lite pull requests som gjorts under veckan. Eftersom jag delegerat uppgiften om att ändra hash_table.c och linked_list.c till att använda referensräknaren så såg jag till att de gjort detta på ett lämpligt sätt. Jag såg en förvirring i att de båda lät destructorn releasea, istället för att låta release kalla på destructorn. Jag uppskattar att folk tar lite av en julpaus i dagsläget så jag är tålmodig med att de korrigerar detta.

Eftersom ett av pull requesten touchar på ganska många filer så tänker jag låta korrigeringar komma in innan jag börjar kolla på att lägga till ny kod själv. En rebase duger i krig men det är skönast om vi slipper konflikter av alla dess slag.

Jag bestämmer mig istället för att lägga lite tid på de olika rapporterna. Ingen massiv ansträngning, men bara lite grundläggande text som vi kan lägga till i senare.
# Lördag 20 December 2025
*Tid: 45 minuter*
Idag fick vi en ny kollega, Marcus. Han ersatte Irfan, som valt att inte delta i projektet. Jag lade ned tid på att uppdatera honom om vårt arbetsflöde, ge honom tillgång till alla nödvändiga kanaler (GitHub, Trello, Discord) och ge honom lite arbetsuppgifter. 

# Torsdag 18 December 2025
*Tid: 120 minuter*
Idag bokade jag in ett möte, en dag tidigt eftersom jag skulle vara upptagen på fredagen. Vi hoppade in på discord 18:00 och hade ett 45 minuters möte där vi pratade lite om vad som hade gått bra och vad som behövde jobbas på. Alla lämnade mötet säkra på sina uppgifter under kommande vecka. Efter mötet satt jag och implementerade cascade limits, så att allocate() inte rekursivt kallar sig själv i all evighet vid exempelvis frigörelse av en länkad lista.
## Mötesanteckningar
### Arbetsroller tills nästa fredag
- Jakob kollar på gprof och gcov makefile shortcuts
- Jakob och Iliya kollar på default destructor och type macros (och cascade limits)
- Alexander kollar vidare på tests
- Alexander och Jonathan kollar på att integrera inlupp 2 i projektet (lägger till mappen i demo, börjar med att ändra hash_table.c och linked_list.c)
- Jonathan kanske börjar kolla på någon av rapporterna. 

### Övrigt
- Försök använda er av flera issues, tänk på att använda existerande markdown i pull request templaten.
- Kom ihåg att hålla Trello syncat till er bästa förmåga
- "Choose the size of your reference counter wisely and document the choice and explain how your system handles (or not) reference counter overflow."

### Administrativt för Jakob
- Maila coach om läget (läget är att Vide inte deltar)
- Lägg till alla rapportuppgifter i Trello
# Onsdag 17 December 2025
*Tid: 90 minuter*
Jag har väntat på Vide med att börja göra retain och release, men tyvärr har han varit väldigt otillräckligt kommunikativ, så jag bestämde mig för att implementera dessa själv. Efter att ha granskat de andras pull requests, accepterat dessa, och läst igenom koden, förstod jag hur mina funktioner skulle fungera. Det tog en dryg timme på grund av sjuka valgrind fel, även fast programmet funkade och inte läckte minne.  

Jag gjorde en pull request med mina nya funktioner, och gjorde även commits som rättade till småfel eller inkompatibilitet i de andras kod. Denna granskades av Alexander och efter han godkände den så mergade jag till main.
# Tisdag 16 December 2025
*Tid: 0 minuter*
Repot blir forkat av övriga gruppmedlemmar och de första pull requestsen kommer in.
# Söndag 14 December 2025
*Tid: 60 minuter*
Jag lade tid på att sätta upp filstrukturen för projektet. Vi bestämde en ungefärlig filstruktur i fredags, så jag utgick från den. Jag skapade utöver det också en pull request template, och började skriva docstrings för RefCounter.h. Jag skrev också en makefile för att kompilera (troligtvis) all kod som kommer skrivas i sprint 1. Detta för att vi imorgon kommer börja arbeta, och ju mer boilerplate som är redo desto mindre kod kommer behöva submittas genom pull requests senare, vilket drar ner på merges från upstream.
Repot är redo att forkas och vi kommer sätta igång imorgon.
# Fredag 12 December 2025
*Tid: 60 minuter*
Ett gruppmöte i discord skedde rum, där jag försökte få alla att ta lite eget ansvar och plats. Jag har egentligen ingen lust att ta mig an ledarrollen. Jag är någon som gärna tar plats och ansvar, men jag föredrar miljöer där en naturlig kooperation uppstår på grund av att alla delar samma driv. Det gäller tyvärr inte här, vilket leder till att jag får ta mycket initiativ åt alla. 

Hursomhelst kom vi fram till lite arbetsfördelning. Jag lovade att sätta upp git repot och filstrukturen samt fylla på i vårt Trello board. Vi beslutade oss för att ta refcountern nu innan jul, och implementationen av den i inlupp 2 efter jul. 
# Torsdag 11 December 2025
*Tid: 45 minuter*
Vi hade gruppmöte med Filip, vår coach för projektet. Vi diskuterade våra framgångar hittills, han kände av lite huruvida han trodde vi var okej förberedda, och det tyckte han. Han saknade däremot en överblick i vår systemarkitektur, något som vi beslutade oss för att ordna imorgon på discord. 
# Onsdag 10 December 2025
*Tid: 60 minuter*
Tillsammans med Alexander och Jonathan satte vi oss ned och började diskutera lite riktlinjer och regler. På grund av att två medlemmar fattades så drev vi protokoll, och tog anteckningar så att alla skulle kunna se i efterhand.
Vi fattade dock inga större beslut om arbetsfördelning, eftersom vi kände att det hade varit bra att ha hela gruppen samlad för det.
# Söndag 7 December 2025
*Tid: 10 minuter*
Jag fick tillgång till vårt GitHub repo och började bjuda in alla gruppmedlemmar till det. 
# Lördag 6 December 2025
*Tid: 25 minuter*
Efter att jag anordnade en omröstning i discord servern beslutade gruppen att vi skulle heta *FooBarnen*. Med detta mailade jag direkt lärare och coach, samt satte upp ett Trello board. Jag annonserade för gruppen att vi fick en tid med coachen på torsdagen den 11:e, och bad gruppen samlas till möte på onsdagskvällen för att snacka ihop oss inför det.
# Onsdag 3 December 2025
*Tid: 20 minuter*
Jag läste igenom instruktionerna översiktligt för att få ett hum om förberedelser som krävdes.
Jag tog på mig att göra en discord server för gruppen. Jag uppmuntrade alla att bidra med ett namn till gruppen och satte lördag som tidsgräns för ett beslut.