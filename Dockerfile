FROM mcr.microsoft.com/playwright/python:v1.45.0-jammy

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# 1. Asennetaan Python-kirjastot backend-kansiosta
COPY backend/requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir playwright && \
    pip install --no-cache-dir -r requirements.txt

# 2. Asennetaan Playwright selaimet
RUN python -m playwright install --with-deps chromium

# 3. Kopioidaan koko projektin koodirakenne
# Tämä luo /app/backend/app/ -rakenteen, jota Python-importit odottavat
COPY backend/ ./backend/

# 4. Asetetaan PYTHONPATH, jotta 'backend' paketti tunnistetaan
ENV PYTHONPATH=/app

# HF vaatii portin 7860
ENV PORT=7860
EXPOSE 7860

# Käynnistys backend-polun kautta
CMD ["uvicorn", "backend.app.api:app", "--host", "0.0.0.0", "--port", "7860"]
