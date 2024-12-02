from pydantic import BaseModel

class ServicoBase(BaseModel):
    nome: str
    descricao: str
    preco: str
    setor: str

class ServicoCreate(ServicoBase):
    pass

class Servico(ServicoBase):
    id: int

    class Config:
        orm_mode = True
