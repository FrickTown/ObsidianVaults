# Kooperativ sandlåda för idéutveckling
## Koncept
Utveckla, planera och designa idéer i realtid med en grupp genom att rita primitiva former, skriva text etc.
## Funktionallitet
- Skapa en 
## Tech stack
### Frontend
- PixiJS för högprestanda WebGL-baserad rendering 
- React / Svelte för UI 
### Backend
- Golang för servern
- Alternativt ha ett host-baserat system, där ledaren av en lobby hostar en server session. 
- Websockets för att kommunicera med klienter. 
### Datahantering
- MongoDB
- Redis
## Concurrencyproblem
- Varje element som placeras har egen metadata. Alla användare ska kunna omplacera och transformera element utan risk för duplicering eller dataförlust, eller inputförl