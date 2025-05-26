# Hot Potato
## Problem
Dagens spel och lekar utövas mer och mer i den digitala världen, framför skärmar och över internet. Många oroar sig över hur mycket tid den genomsnittliga människan stirrar på skärmar varje dag, och vidare är vissa helt övertygade om skärmtidens direkt negativa effekter på det mänskliga psyket, och särskilt unga psyken. 
Fler semi-digitala lösningar för spel hade kunnat uppmuntra en mer balanserad livsstil i både barn och vuxna. 
## Beskrivning
Spelet går ut på att en av 2+ spelare blir tilldelade en "bomb". Spelaren som har bomben måste kasta den ifrån sig till en av de andra spelarna innan den sprängs. Bombens stubin är representerad med en progressivt snabbare blinkande LED-skärm. Spelaren som håller i bomben när den "sprängs" åker ur spelet. När endast en spelare är kvar i spelet har vinnaren blivit utsedd.
## Krav
#### Kort sammanfattning av alla komponenter:
- Spelet kräver minst 2 spelare och en server.  
- Spelets konfiguration börjar när servern startar.  
- Klienter som vill delta anropar servern och blir tilldelade ett ID.  
- Servern startar spelet, och ger en “bomb” till en av spelarna.  
- Bomben, vars stubin ständigt krymper (representerad här med blinkande LED-lampor), måste nu kastas runt bland spelarna (med en faktisk kast-motion). Det är otydligt hur långt det är kvar på stubinen, som kan krympa olika fort varje rond enligt en randomiserad funktion, alltså inte alltid linjärt.
- Kast-motionen ska med fördel även inkorporera kompass för att avgöra vem kastet går till. Detta går att implementera på många sätt.
- Vinner gör den som inte håller bomben när den smäller, och som står ensam kvar bland deltagarna.
- Den som förlorar blir kickad från servern och kan inte längre få bomben förrän en vinnare utsetts och en ny omgång startat.
<p style="page-break-after: always;"></p>
#### Hur detta bemöter det påstådda problemet:
Spelet är ett semi-digitalt, semi-fysiskt socialt spel, och spelas i en formation där alla kollar på varandra. Alla spel och lekar som spelas utanför den exklusivt digitala världen kan anses vara lösningar på det uppfattade problemet.
Eftersom spelet har väldigt lätta regler, och skapar artificiell stress - och således emotionellt engagemang - så kan det exempelvis användas som en isbrytare med nya bekanta, som annars har en tendens att vara lite timida.
#### Hur detta uppfyller uppgiftskraven:
- Programmet skall delas upp i **funktioner**.  
- Server-klient kommunikation använder **radiofunktionen**.  
- Spelet kräver minst **två spelare** och en **dedikerad server** ***(3 microbits)***  
- Spelet producerar **utdata** både i form **stubinen** och **vem som vunnit**.  
- Spelet använder sig av **extern** **stimuli** i form av **accelerometern** och **kompassen**.
… och kommer motvilligt göras med **Blockprogrammering**…

## Slutdemonstration
Med spelets enkla regler i åtanke, och spelets modulära antal deltagare (2 till n, n är teoretiskt väldigt stort, endast begränsat av precisionen av microbit-sensorerna. Gissningsvis går gränsen kanske på omkring 6) så borde ett antal volontärer från publiken kunna delta i en speldemonstration. 