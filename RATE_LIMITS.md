# Rate Limiting Configuration

## Suositellut rajat portfoliodemoon (Rekrytoijat)

Nämä rajat on optimoitu niin, että rekrytoija voi testata kaikki ominaisuudet rauhassa, mutta väärinkäyttö estyy:

### Agenttirajat (Sales, Research, Meeting Prep)
- **5 kutsua / 15 minuuttia** - Riittää kaikkien kolmen agentin testaamiseen + uudelleenyritykset
- **10 kutsua / tunti** - Mahdollistaa perusteellisen testauksen
- **25 kutsua / päivä** - Antelias päiväraja demokäyttöön

### Yleiset API-rajat (Auth, Config, yms.)
- **30 kutsua / minuutti** - Normaali käyttö
- **500 kutsua / tunti** - Estää automaattiset hyökkäykset

## Miksi nämä rajat?

✅ **Rekrytoija-ystävällinen:**
- Voi testata jokaisen agentin (3 agenttia × 2 testiä = 6 kutsua)
- Aikaa kokeilla eri syötteitä
- Ei tarvitse odotella testien välillä

🛡️ **Turvallisuus:**
- Estää API-avaimen väärinkäytön
- Suojaa Gemini/Tavily ilmaiskiintiöt
- Botin hyökkäys ei kaada palvelua

💰 **Kustannustehokas:**
- Gemini free tier: 15 req/min, 1500 req/päivä
- Tavily free tier: 1000 hakua/kk
- 25 agenttikutsua/päivä = ~75 API-kutsua (hyvin kiintiöiden sisällä)

## Käyttöönotto

### Backend (jo käytössä)
Rajat on määritelty tiedostossa: `backend/app/middleware/rate_limiter.py`

### Muokkaus (jos tarpeen)
Voit säätää rajoja muuttamalla `rate_limiter.py` tiedoston `self.limits` -sanakirjaa:

```python
self.limits = {
    "agent": {
        "per_15min": 5,   # Muuta tätä
        "per_hour": 10,   # Muuta tätä
        "per_day": 25,    # Muuta tätä
    },
    "general": {
        "per_minute": 30,
        "per_hour": 500,
    }
}
```

### Renderissä (tuotanto)
Ei tarvitse tehdä mitään - rajat ovat koodissa. Voit halutessasi lisätä environment variablen:
```
RATE_LIMIT_ENABLED=true
```

## Virheilmoitukset käyttäjille

Kun raja ylittyy, käyttäjä näkee selkeän viestin:

```
⏱️ Rate limit exceeded: 5 agent requests per 15 minutes. 
Please wait before trying again.

This is a demo application with usage limits to prevent abuse. 
Thank you for understanding!
```

## Seuranta

Rate limiter lisää HTTP-headerit jokaiseen vastaukseen:
- `X-RateLimit-Remaining-15min` - Jäljellä olevat kutsut (15 min)
- `X-RateLimit-Remaining-Day` - Jäljellä olevat kutsut (päivä)

Voit tarkistaa nämä selaimen Developer Tools → Network -välilehdeltä.
