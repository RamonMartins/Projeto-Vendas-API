from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, SessionLocal

# Cria as tabelas ainda não criadas no banco
models.Base.metadata.create_all(bind=engine)

# Inicia a aplicação
app = FastAPI()

# Cria uma sessão com o Banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para Criar Produto
@app.post("/produtos/", response_model=schemas.ProdutoResponse)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    db_produto = models.Produto(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto