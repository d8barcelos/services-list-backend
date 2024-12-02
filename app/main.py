from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Divulgação de Serviços")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao sistema de divulgação de serviços!"}

@app.post("/servicos/", response_model=schemas.Servico)
def criar_servico(servico: schemas.ServicoCreate, db: Session = Depends(get_db)):
    return crud.criar_servico(db=db, servico=servico)

@app.get("/servicos/", response_model=list[schemas.Servico])
def listar_servicos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.listar_servicos(db=db, skip=skip, limit=limit)

@app.get("/servicos/{servico_id}", response_model=schemas.Servico)
def obter_servico(servico_id: int, db: Session = Depends(get_db)):
    db_servico = crud.obter_servico(db=db, servico_id=servico_id)
    if db_servico is None:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    return db_servico
