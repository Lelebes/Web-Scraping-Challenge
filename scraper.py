import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

# Config do Banco
class Base(DeclarativeBase):
    pass

class Noticia(Base):
    __tablename__ = "noticias"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(255))
    link: Mapped[str] = mapped_column(String(500))

# Cria o banco local
engine = create_engine("sqlite:///dados_g1.db")
Base.metadata.create_all(engine)

def extrair_dados_g1():
    url = "https://g1.globo.com/tecnologia/"
    
    # Header pra evitar bloqueio
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"Erro na requisição: {e}")
        return

    soup = BeautifulSoup(r.text, "html.parser")
    # Seletores das notícias do G1
    posts = soup.find_all("div", class_="feed-post-body")
    
    noticias = []

    for post in posts:
        link_tag = post.find("a", class_="feed-post-link")
        
        if link_tag:
            titulo = link_tag.get_text().strip()
            link = link_tag.get("href")
            
            noticias.append(
                Noticia(titulo=titulo, link=link)
            )

    # Salva tudo no banco
    if noticias:
        with Session(engine) as session:
            session.add_all(noticias)
            session.commit()
            print(f"Sucesso: {len(noticias)} itens salvos.")
    else:
        print("Nada encontrado.")

if __name__ == "__main__":
    extrair_dados_g1()