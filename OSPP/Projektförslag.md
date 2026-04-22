# Kooperativ sandlåda för idéutveckling
## Koncept
Utveckla, planera och designa idéer i realtid med en grupp genom att rita primitiva former, skriva text, skapa flowcharts etc. Tänk canva, fast med högre prestanda, bättre tillgänglighet, mer frihet, och mindre tjockt. Mer för snabb prototyping (och eventuellt nöje)
## Funktionallitet
- Skapa ett nytt projekt
- Skapa nya projektdelar (ritningar)
- Operera på olika lager i en ritning 
- Konto ska inte krävas för att skapa projekt, men kan användas för att spara flera projekt till en plats.
- Dela enkelt projektlänk med andra
- Lås projekt med lösenord
- Rendera till PDF 
## Tech stack
### Frontend
- PixiJS för högprestanda WebGL-baserad rendering 
- React / Svelte för UI 
### Backend
- Golang för servern
	- Alternativt ha ett host-baserat system, där ledaren av en lobby hostar en server session. 
- Websockets för att kommunicera mellan server och klienter. 
### Datahantering
- MongoDB
- Eventuellt något caching-system såsom redis om nödvändigt
## Concurrencyproblem
- Varje element som placeras har egen metadata. Alla användare ska kunna omplacera och transformera element utan risk för duplicering eller dataförlust, samt inputförlust. 