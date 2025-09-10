from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Produto(BaseModel):
    nome: str
    preco: float
    disponivel: bool


@app.get("/")
def root():
    return "Olá mundo!!"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/produtos/")
def criar_produto(item: Produto):
    return {"mensagem": "Produto criado!", "dados": item, "nome": item.nome}