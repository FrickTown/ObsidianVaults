# M39: Pekare till pekare
##### Jakob Frick | 04-11-2025

## Inledning
Pekare har i decennier frustrerat aspirerande datavetare. Det räcker med en snabbtitt på YouTube för att förstå det. Det finns otaliga videos med försök till att förklara konceptet — och antalet visningar når miljoner på somliga. Så vadan förvirringen? Jo, i högnivåspråk, såsom ***Python*** och ***Java***, behöver inte programmeraren hantera lagring och rensning av data i minnet. I dessa mer nybörjarvänliga språk är pekarlogiken kvar, men undangömd och automatiserad. Så när en intermediärt erfaren programmerare är redo att ta sig an ett lågnivåspråk som C (där pekare är väldigt centralt), så bemöts denne av ett helt nytt lager av logik, som ofta kan utmana ens tidigare uppfattningar om programmering. 
## Bakgrund
Så vad är en pekare? Kort sagt: 

> En pekare är en datatyp, som en ***integer***, eller en ***float***, men istället för ett aritmetiskt siffervärde eller datastruktur, så är pekarens värde en minnesadress. Och den minnesadressen tillhör en plats i minnet där ett värde av någon förutbestämd typ kan återfinnas. 

För en som suttit med pekare en stund så är denna förklaring godtycklig. En nybörjare är nog precis lika förvirrad med denna förklaring som utan den. Men även någon som suttit med pekare en stund kan bli förvirrad av *pekare till pekare* (hädanefter kallad dubbelpekare).

Så vad är en dubbelpekare? 
>En dubbelpekare är variabel vars värde är adressen till en annan plats i minnet, en plats som innehåller ett värde som är av typen pekare.

Svårare än så är det inte. Men vad är ens poängen? Vilka användningsområden har dubbelpekare, och hur går en sådan implementation till?
## Syfte
Man kan använda dubbelpekare överallt om man verkligen vill överkomplicera sin kod. Dock är det väldigt sällan som det faktiskt ***behövs***. Om vi har en pekare till något datum, och vi har en referens till den pekaren, så kan vi ändra vilket datum pekaren pekar på. Om vi också har en pekare till pekaren, så kan vi totalt ändra vilken pekare som ligger på just den platsen i minnet. En vanlig applikation för dubbelpekare är i logiken för länkade datastrukturer, där det kan användas för att sätta in, eller ta bort noder, i väldigt få rader kod. Denna redovisning av mål M39 beskriver skapandet av en *iterator för en länkad lista*, och de två väsentliga funktionerna *insert* och *remove*. 
## Genomförande
Vi börjar med att definiera våra typer. 
```c
typedef struct node node_t;

struct node {
	int value;
	node_t* next;
}

typedef struct list list_t;

struct list {
	node_t* first;
	uint size;
}

typedef struct iterator iterator_t;

struct iterator {
	list_t*  list;
	node_t** current; 
}
```
En nod består av ett värde, och mest relevant, en pekare till sin eventuella efterträdare. En iterator består av en pekare till listan den är kopplad till, samt en dubbelpekare till den nuvarande noden. Vi kommer snart se varför. För koncishetens skull så skippar jag att definiera alla funktioner för listan. Det är bara en startpunkt på en kedja av noder som pekar på sin efterträdare.

Så, antag nu att en lista `testlist` skapas med 4 noder, vars värde motsvarar dess plats i listan. Antag också att vi har skapat en iterator `iter`, och länkat den med `testlist`. Funktionerna `next`, `insert` och `remove` kan nu implementeras på följande sätt:
```c
list_t testlist = make_list_of_size(4);
iterator_t iter = make_iterator(testlist);

void iterator_next(iterator_t* iter) {
	if(iterator_has_next(iter)) {  
	    iter->current = &((*(iter->current))->next);  
	    return (*(iter->current))->data;  
	}  
	iter->current = NULL;  
	return;
}

void iterator_insert(iterator_t* iter, int val) {
	node_t* new_node = make_node(val, cur_node);
	node_t* cur_node = *(iter->current);
	new_node->next = cur_node;
	(*(iter->current)) = new_node;
	iter->list->size += 1;
}

int iterator_remove(iterator_t* iter) {
	link_t* to_remove = *(iter->current);  
	link_t* next = to_remove->next;  
	elem_t val = to_remove->data;
	*iter->current = next;
	free(to_remove);
	iter->list->size -= 1:
}
``` 

Med bara några enstaka rader kod kan vi uppnå två ganska komplexa operationer. Detta är förstås dock för en väldigt minimal implementation av listan. 
## Hur funkar detta?
En iterators current-värde är alltid en pekare till en nods next-värde. Och en nods next-värde är alltid ett alias av en pekare som skapas när vi skapar en efterträdande nod med make_node. När vi vill nå vår "current" nod, går vi alltså igenom en pekare till dess företrädares next-värde. Denna referens kommer därmed tillåta oss att alltså ha kontroll över vilken nod vår "current" nods företrädare anser som sin efterträdare. 

**Diagram här**
Detta är onekligen en vettig användning av dubbelpekare. En mer naiv lösning för att få funktioner som insert och remove att funka i denna kontext är att låta iterator-typen också hålla koll på sin "föregående".
## Implementation i eget program


## Slutsats