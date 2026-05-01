# Usa a versão slim pra imagem não ficar gigante
FROM python:3.11-slim

WORKDIR /app

# Copia o requirements primeiro pra aproveitar o cache de camadas do Docker
COPY requirements.txt .

# Instala pacotes sem guardar cache do pip (ajuda a manter a imagem leve)
RUN pip install --no-cache-dir -r requirements.txt

# Agora sim joga o resto do código pra dentro
COPY . .

CMD ["python", "scraper.py"]