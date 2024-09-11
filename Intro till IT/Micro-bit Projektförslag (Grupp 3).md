# Hot Potato
## Problem
Dagens spel och lekar utövas mer och mer i den digitala världen, framför skärmar och över internet. Fler 
## Beskrivning
Spelet går ut på att en av 2+ spelare blir tilldelade en "bomb". Spelaren som har bomben måste kasta den ifrån sig till en av de andra spelarna innan den sprängs. Bombens stubin är representerad med en progressivt snabbare blinkande LED-skärm. Spelaren som håller i bomben när den "sprängs" åker ur spelet. När endast en spelare är kvar i spelet har vinnaren blivit utsedd.
## Krav
#### Kort sammanfattning av alla komponenter:
- Spelet kräver minst 2 spelare och en server.  
- Spelets konfiguration börjar när servern startar.  
- Klienter som vill delta anropar servern och blir tilldelade ett ID.  
- Servern startar spelet, och ger en “bomb” till en av spelarna.  
- Bomben, vars stubin ständigt krymper (representerad här med blinkande LED-lampor), måste nu kastas runt bland spelarna (med en faktisk kast-motion). Det är otydligt hur långt det är kvar på stubinen, som kan krympa olika fort varje rond enligt en randomiserad funktion.  
- Vinner gör den som inte håller bomben när den smäller, och som står ensam kvar bland deltagarna.
- Den som förlorar blir kickad från servern och kan inte längre få bomben, tills någon är ensam kvar på servern.
#### Hur detta uppfyller kraven:
- Programmet skall delas upp i **funktioner**.  
- Server-klient kommunikation använder **radiofunktionen**.  
- Spelet kräver minst **två spelare** och en **dedikerad server** ***(3 microbits)***  
- Spelet producerar **utdata** både i form **stubinen** och **vem som vunnit**.  
- Spelet använder sig av **extern** **stimuli** i form av **accelerometern** och **kompassen**.
… och kommer motvilligt göras med **Blockprogrammering**…