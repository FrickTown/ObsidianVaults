## Fall 1:
Grundoperationer:
- Jämföra vikter
- Skapa delmängder av samlingar
Alternativ a: Divide and conquer
Alternativ b: 
- Dela upp i grupper om 3,3,2,
- Väg alla delsamlingar,
- Om 3x3 är ojämna är det ett av dem, är de jämna så är det en av de resterande 2.
Alternativ c: Random urval av 2 stycken ägg, nedre gräns blir en aktion.

## Fall 2:
Samma som ovan... Fast med 16 ägg => Delgrupper 5,5,6.
## Fall 3:
Divide and conquer är enda reliable. 
## Fall 4: 
1.  Selection Sort-liknande
	1. Välj en vikt (random ägg)
	2. Jämför alla resterande ägg individuellt mot vikten
	3. Om minst ett ägg väger mindre än vikten så är vikten rutten och bör inkluderas i delmängden som slängs. Om minst ett ägg väger mer än vikten så är vikten inte rutten, och bör exkluderas. 
	4. Problem uppstår när alla är ruttna eller ingen är rutten.
2. 