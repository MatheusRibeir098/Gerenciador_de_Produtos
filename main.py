from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi.staticfiles import StaticFiles

# --- Configuração do Banco de Dados (SQLite) ---
DATABASE_URL = "sqlite:///./loja.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- Modelo (Tabela de Produtos) ---
class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    preco = Column(Float)
    categoria = Column(String)

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

# --- App FastAPI ---
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Dependência para pegar a sessão do DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Rotas (CRUD) ---

# R: READ (Ler/Listar)
@app.get("/")
def ler_produtos(request: Request, db: SessionLocal = Depends(get_db)):
    produtos = db.query(Produto).all()
    return templates.TemplateResponse("index.html", {"request": request, "produtos": produtos})

# C: CREATE (Criar)
@app.post("/adicionar")
def adicionar_produto(nome: str = Form(...), preco: float = Form(...), categoria: str = Form(...), db: SessionLocal = Depends(get_db)):
    novo_produto = Produto(nome=nome, preco=preco, categoria=categoria)
    db.add(novo_produto)
    db.commit()
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

# U: UPDATE (Editar - Simplificado via form) - Rota para carregar form de edição
@app.get("/editar/{id}")
def form_editar(request: Request, id: int, db: SessionLocal = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    return templates.TemplateResponse("index.html", {"request": request, "produto_editar": produto})

# U: UPDATE (Salvar a edição)
@app.post("/atualizar/{id}")
def atualizar_produto(id: int, nome: str = Form(...), preco: float = Form(...), categoria: str = Form(...), db: SessionLocal = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    produto.nome = nome
    produto.preco = preco
    produto.categoria = categoria
    db.commit()
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

# D: DELETE (Deletar)
@app.get("/deletar/{id}")
def deletar_produto(id: int, db: SessionLocal = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if produto:
        db.delete(produto)
        db.commit()
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)