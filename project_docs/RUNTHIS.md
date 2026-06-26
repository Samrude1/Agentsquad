# 🚀 PIKAKÄYNNISTYS-OHJE (Start here)

Jos palaat tämän projektin pariin tauon jälkeen, tässä on minimivaiva-ohje jolla saat kaiken päälle 30 sekunnissa.

---

### 1. Backend (API) päälle
Avaa uusi terminaali ja aja:
```powershell
.\.venv\Scripts\activate
uvicorn backend.app.api:app --reload
```
*API pyörii nyt osoitteessa: http://localhost:8000*

---

### 2. Frontend (Käyttöliittymä) päälle
Avaa **toinen** terminaali (klikkaa `+` nappia terminaalissa) ja aja:
```powershell
cd frontend
npm run dev
```
*UI pyörii nyt osoitteessa: http://localhost:5173*

---

### 3. Kirjautuminen
Mene selaimella osoitteeseen **[http://localhost:5173](http://localhost:5173)**.
- **PIN-koodi:** `0000` (oletus)

---

### 💡 Muistilista jos jokin mättää:
- **Python:** Käytä AINA virtuaaliympäristöä (`.venv`). Projekti vaatii Python 3.12 tai 3.13 (ei toimi 3.14 versiolla).
- **API-avaimet:** Varmista että juurikansiossa on `.env` tiedosto ja siellä on voimassa oleva `OPENAI_API_KEY` (Gemini API avain käy).
- **Portit:** Jos saat "Port in use" virheen, jokin vanha prosessi on jäänyt päälle. Sulje terminaalit ja yritä uudestaan.

### 🛡️ Rate Limiting (Portfoliodeploymenttia varten)
Projekti sisältää valmiin rate limiting -suojauksen:
- **5 agenttikutsua / 15 min** (riittää kaikkien agenttien testaamiseen)
- **10 agenttikutsua / tunti**
- **25 agenttikutsua / päivä**

Katso tarkemmat tiedot: `RATE_LIMITS.md`

Testaa rate limiting paikallisesti:
```powershell
.\.venv\Scripts\python test_rate_limits.py
```


---
*Samantien valmista! 🤖*
