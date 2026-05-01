# Web Scraping Challenge - Trimon

Script simples em Python para coletar as últimas notícias da editoria de tecnologia do G1 e salvar em um banco de dados local.

## O que o projeto faz

- Acessa a página de tecnologia do G1.
- Extrai títulos e links das notícias principais.
- Salva os dados em um banco SQLite usando SQLAlchemy.

## Tecnologias usadas

- Python 3
- BeautifulSoup4 (parsing de HTML)
- SQLAlchemy (ORM para persistência)
- Requests (requisições HTTP)

## Como rodar

1. Crie o ambiente virtual:

```bash
python -m venv venv
```

2. Ative o venv:
   Windows: .\venv\Scripts\activate
   Linux/Mac: source venv/bin/activate

3. Instale as dependências:
   pip install -r requirements.txt

4. Execute o scraper:
   python scraper.py

O arquivo dados_g1.db será criado na pasta com as informações coletadas. Você pode usar um visualizador de SQLite para conferir os dados.
