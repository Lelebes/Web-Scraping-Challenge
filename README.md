# Web Scraping Challenge - Escavador (Equipe Trimon)

Este é um script em Python desenvolvido para coletar as últimas notícias da editoria de tecnologia do G1 e persistir os dados em um banco de dados local. O objetivo deste projeto é demonstrar a construção de um pipeline de dados funcional, utilizando boas práticas de organização e containerização.

## O que o robô faz

- Realiza o scraping da página de tecnologia do portal G1.
- Extrai títulos e links das notícias principais via seletores HTML.
- Persiste as informações de forma estruturada em um banco SQLite.

## Ferramentas utilizadas

- Python 3.11+
- BeautifulSoup4: Parsing de HTML e extração de dados.
- SQLAlchemy: ORM para manipulação do banco de dados (Sintaxe 2.0).
- Requests: Gerenciamento de requisições HTTP.
- Docker: Containerização para garantir a portabilidade do ambiente.

## Como rodar o projeto

### Opção 1: Via Docker (Recomendado)

Se você tem o Docker instalado, não precisa configurar o Python manualmente. Basta rodar no terminal:

1. Build da imagem:
   `docker build -t scraper-escavador .`

2. Execução do container:
   `docker run --name bot-g1 scraper-escavador`

---

### Opção 2: Instalação Local

Caso prefira rodar direto na máquina, siga os passos abaixo:

1. Crie o ambiente virtual (venv):
   `python -m venv venv`

2. Ative o venv:
   Windows: `.\venv\Scripts\activate`
   Linux/Mac: `source venv/bin/activate`

3. Instale as dependências:
   `pip install -r requirements.txt`

4. Execute o script:
   `python scraper.py`

## Observações técnicas

- O arquivo `dados_g1.db` será gerado automaticamente na primeira execução.
- O código utiliza o SQLAlchemy para garantir que a estrutura do banco seja criada via código (migrations-ready), facilitando a manutenção futura do pipeline.
