# Agent Squad – Deployment Walkthrough 🚀

Tämä dokumentti kuvaa, miten **Agent Squad** -alusta on siirretty paikallisesta kehitysympäristöstä pilveen hyödyntäen kustannustehokkaita (0 €) moderneja alustoja.

## Arkkitehtuuri
- **Backend:** FastAPI (Python) – Docker-kontitettu Playwright-ympäristö.
- **Frontend:** React (Vite) – Staattinen SPA dynaamisilla API-kutsuilla.
- **Hosting:** 
  - Backend: Hugging Face Spaces (Docker)
  - Frontend: Vercel

---

## 1. Backend – Hugging Face Spaces (Docker)

Backend vaatii monimutkaisia kirjastoja (Playwright, Chromium), joten Docker on paras tapa varmistaa toimivuus pilvessä.

### Konfiguraatio
Projektin juuressa on `Dockerfile`, joka:
1. Käyttää `mcr.microsoft.com/playwright/python` -pohjaa.
2. Asentaa riippuvuudet (`requirements.txt`).
3. Rakentaa koodin vaatiman `backend/app` -kansiorakenteen.
4. Käynnistää Uvicorn-palvelimen portissa **7860** (HF Spacesin vaatimus).

### Turvallisuus & Secrets
Kaikki herkät tiedot on siirretty HF Spacen **Settings → Variables and secrets** -osioon:
- `OPENAI_API_KEY`: Agenttien äly (Gemini 2.0 Flash).
- `TAVILY_API_KEY`: Hakuagenttien työkalut.
- `APP_PIN`: Käyttöliittymän pääsynvalvonta.
- `FRONTEND_URL`: CORS-suojaus (Vercel-sivuston osoite).

---

## 2. Frontend – Vercel

Frontend on dynaaminen React-sovellus, joka keskustelee backend-APIn kanssa.

### API-integraatio
Käytössä on `getApiUrl()` -utiliteetti, joka havaitsee ympäristön:
- **Local:** `http://localhost:8000`
- **Prod:** Vercelin `VITE_API_URL` -ympäristömuuttuja.

### Julkaisu
1. Yhdistetty GitHub-repository Verceliin.
2. Asetettu `Root Directory` arvoksi `frontend`.
3. Lisätty `VITE_API_URL` osoittamaan HF Space -osoitteeseen.

---

## 3. Lopputulos
Agent Squad tarjoaa täyden agentti-orkestraation ilman kalliita palvelinkustannuksia. Järjestelmä on skaalautuva, suojattu PIN-koodilla ja raportit tallentuvat automaattisesti käsiteltävään muotoon.

> [!NOTE]
> Tämä dokumentti on tarkoitettu esimerkiksi siitä, miten monimutkainen AI-sovellus viedään tuotantoon hyödyntäen ilmaisia työkaluja ammattimaisella tavalla.
