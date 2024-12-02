from sqlalchemy.orm import Session
from app import models, schemas

def criar_servico(db: Session, servico: schemas.ServicoCreate):
    db_servico = models.Servico(nome=servico.nome, descricao=servico.descricao, preco=servico.preco, setor=servico.setor)
    db.add(db_servico)
    db.commit()
    db.refresh(db_servico)
    return db_servico

def listar_servicos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Servico).offset(skip).limit(limit).all()

def obter_servico(db: Session, servico_id: int):
    return db.query(models.Servico).filter(models.Servico.id == servico_id).first()
