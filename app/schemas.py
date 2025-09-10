from pydantic import BaseModel, ConfigDict

class ProdutoBase(BaseModel):
    nome: str
    preco: float
    disponivel: bool = True

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)