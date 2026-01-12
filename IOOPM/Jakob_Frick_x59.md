# Vem pekar du på? Och vem pekar de på?
<span style="font-size: 1.3em; margin-left: 2em;">En redovisning av M39: Pekare till pekare</span>
<span style="font-size: 1em; margin-left: 4.1em;">Jakob Frick | 2025-12-11</span>

## Inledning
Pekare har i decennier frustrerat aspirerande datavetare. Det räcker med en snabbtitt på YouTube för att förstå det. Det finns otaliga videos med försök till att förklara konceptet — och antalet visningar når miljoner på somliga. Så vadan förvirringen? Jo, i högnivåspråk, såsom *Python* och *Java*, behöver inte programmeraren hantera lagring och rensning av data i minnet. I dessa mer nybörjarvänliga språk är pekarlogiken kvar, men undangömd och automatiserad. Så när en intermediärt erfaren programmerare är redo att ta sig an ett lågnivåspråk som C (där pekare är väldigt centralt), så bemöts denne av ett helt nytt lager av logik, som ofta kan utmana ens tidigare uppfattningar om programmering. 

Så vad är en pekare? Kort sagt: 

> En pekare är en datatyp, som en ***integer***, eller en ***float***, men istället för ett aritmetiskt siffervärde eller datastruktur, så är pekarens värde en minnesadress. Den minnesadressen tillhör en plats i minnet där ett värde av någon förutbestämd typ förväntas kunna återfinnas. Pekarvariabler betecknas i C med en asterisk (*) före sitt namn. Exempelvis `int* p` eller `int *p`.

För en som suttit med pekare en stund så är denna förklaring godtycklig. En total nybörjare till programmering löper däremot risk att vara lika förvirrad med denna förklaring som utan den. Men även någon som suttit med pekare en stund kan bli förvirrad av *pekare till pekare* (hädanefter kallad dubbelpekare).

Så vad är en dubbelpekare? 
>En dubbelpekare är variabel av typen pekare, vars värde är adressen till en annan plats i minnet, en plats som innehåller ett värde som också är av typen pekare. Dubbelpekare betecknas rimligtvis med två asterisker (**).

Svårare än så är det inte. Men vad är ens poängen? Vilka användningsområden har dubbelpekare, och hur går en sådan implementation till?
## Syfte
Man kan använda dubbelpekare överallt om man verkligen vill överkomplicera sin kod. Dock är det väldigt sällan som det faktiskt *behövs*. Om vi har en referens till en pekare till något datum, så kan vi ändra datumet på platsen i minnet som pekaren pekar på. Om vi vidare har en pekare till *den* pekaren, så kan vi totalt ändra vilken pekare som ligger på just den platsen i minnet. En vanlig applikation för dubbelpekare är i logiken för länkade datastrukturer, där det kan användas effektivt för att sätta in, eller ta bort noder. Denna redovisning av mål M39 beskriver skapandet av en iterator för en länkad lista, och de tre väsentliga funktionerna `next()`, `insert()` och `remove()`. 

<div style="page-break-after: always;"></div>

## Genomförande
Vi börjar med att definiera våra typer. 
```c
typedef struct node node_t;

struct node {
	int value;
	node_t* next;
};

typedef struct list list_t;

struct list {
	node_t* first;
	int size;
};

typedef struct iterator iterator_t;

struct iterator {
	list_t*  list;
	node_t** current; 
};
```
#### *Kodblock 1 - Typdefinitioner för en länkad lista, dess noder, och en iterator.*

En `node` består av ett värde, och mest relevant, en pekare till sin eventuella efterträdare. En `iterator` består av en pekare till listan den är kopplad till, samt en dubbelpekare till den nuvarande noden. För koncishetens skull så definieras inte alla funktioner för listan. Det är bara en startpunkt på en kedja av noder som pekar på sina respektive efterträdare.

Så, antag nu att en lista `testlist` skapas med 4 noder, vars värde motsvarar dess plats i listan. Antag också att vi skapar en iterator `iter`, och länkar den med `testlist`. Funktionerna `next`, `insert` och `remove` kan nu implementeras på följande sätt:
```c
// En lista med fyra noder skapas, varje nod får ett slumpat värde
list_t testlist = make_list_of_size(4);
// En nyskapad iterators current-värde pekar till next-värdet av listans första nod.
iterator_t iter = make_iterator(testlist);

int iterator_next(iterator_t* iter) {
	// iterator_has_next avgör om det finns ett till element i listan
	if(iterator_has_next(iter)) {  
		// Vi kan få nästa dubbelpekare med dessa steg
		node_t* ptr_to_current = *(iter->current);
		node_t* currents_next = ptr_to_current->next;
		node_t** ptr_to_currents_next = &currents_next;
		iter->current = ptr_to_currents_next;

		// Eller sammanvävt:
	    iter->current = &((*(iter->current))->next);  
	    return (*(iter->current))->value;  
	}  
	iter->current = NULL; // Om vi nått slutet på listan 
    return -1;
}

void iterator_insert(iterator_t* iter, int val) {
	node_t* ptr_to_current = *(iter->current);
	// Skapar en ny nod med givet value, samt ett givet next-värde
	node_t* new_node = make_node(val, ptr_to_current);
	(*(iter->current)) = new_node;
	iter->list->size += 1;
}

int iterator_remove(iterator_t* iter) {
	node_t* to_remove = *(iter->current);  
	node_t* next = to_remove->next;  
	int val = to_remove->value;
	*iter->current = next;
	// Friar en nodpekare säkert
	destroy_node(to_remove);
	if(--iter->list->size == 0) {
		iter->list->first = NULL;
	}
	return val;
}
``` 
#### *Kodblock 2 - Implementationer av de iteratorfunktionerna mest relevanta för mål m39.*

Med bara några enstaka rader kod kan vi uppnå två ganska komplexa operationer. Detta är förstås för en väldigt minimal implementation av iteratorn och listan, som inte hanterar några edge-cases. Att tänka ut dessa, samt skydd mot dem, lämnas till läsaren.

### Hur fungerar detta?
En iterators `current` är alltid en pekare till en nods `next`, och som vi ser i *Diagram 1*, är en nods `next` alltid ett alias av en pekare som skapas när vi skapar en efterträdande nod med `make_node`. Trots att iteratorns dubbelpekare heter current, kan man föreställa sig att iteratorn i själva verket pekar på en del av noden som *företräder* noden vi egentligen kallar "current", även om det är faktiskt där vi hamnar om vi följer dubbelpekaren fullt ut.

![Diagram_Före](./Diagram1_Före.png)
#### *Diagram 1 - En typisk länkad lista med fiktiva minnesvärden.*

Om vi föreställer oss att en `node` delar på sina 4 bytes av minne jämnt (demonstreras i första noden av *Diagram 2*), då har vi alltså två delar: `0x00` - `0x01` som innehåller strängen (nodens `value`), och `0x02` - `0x03` som innehåller pekaren (nodens `next`). Om vi skulle ha en pekare till platsen `0x02` och sätta den som vår iterators current-värde, så kan vi *både* ta två steg för att hamna på `0x04` och läsa och skriva till vår "current" node, *och* skriva till `0x02` - vilket är next-värdet av vår "current" nodes företrädare. 

![Diagram_Före](./Diagram2.png)
#### *Diagram 2 - Den länkade listan, med första nodens minne uppdelat i segment, och en ny pekare som representerar iteratorns current-värde (markerad i lila färg).*

Om vi, som i *Diagram 3*, ändrar pekaren på `0x02` till att istället ha värdet `0x08`, så är det endast pekaren som finns vid `0xc4` som pekar på noden, vilket innebär att den kan frias. Plötsligt har vi blivit av med en nod i listan.

![Diagram_Före](./Diagram3.png)
#### *Diagram 3 - Den länkade listan, med första nodens pekare nu inställd på 0x08, vilket uppnåddes med hjälp av referensen till iteratorns current-värde. Detta tillåter frigöring av pekaren vid 0xc4.*

Detta är onekligen en vettig användning av dubbelpekare. En mer naiv lösning för att få funktioner som `insert` och `remove` att funka i denna kontext med *enkelpekare* istället för dubbelpekare, är att låta iterator-typen även hålla koll på sitt föregående current-värde. Det leder dock till mer verbos och potentiellt mer svårläst kod, speciellt när man börjar implementera hantering för edge-cases.

## Resultat
I mitt egna program ville jag ha en mer "barnsäker" iterator. Främst ville jag att om iteratorn befinner sig på sista elementet i listan, så ska `remove()` kunna användas upprepat för att kontinuerligt plocka bort det sista elementet, ända tills listan är tom. Det ledde till en `remove()` som är lite mer verbos än implementationen ovan. Sägas bör, dock, att när jag bytte från en enkel- till en dubbelpekare för `iter.current`, så gick min implementation av `remove()` från 50 rader, till 25 rader kod, ett klart bevis för att det finns ett värde i dubbelpekare.

## Avslutning
Att behöva tänka på minne är något många programmerare helst väljer att slippa. För en som verkligen gillar kontroll, och som kanske uppskattar det extra lagret med logik som en ytterligare utmaning, så är pekare det perfekta verktyget. Att kunna använda dubbelpekare krävs kanske sällan för att lösa ett problem. Trots det, så är det viktigt för en duktig lågnivåprogrammerare att kunna konceptualisera pekare till pekare. För när möjligheten att använda en uppstår, så är det inte bara tragiskt att missa den, det kan mycket väl vara den mest optimala lösningen. 