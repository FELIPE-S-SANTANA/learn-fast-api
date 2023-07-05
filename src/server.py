from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from typing import List
from uuid import uuid4

app = FastAPI()
origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


class Animais(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str
    cor: str

banco: List[Animais] = []

@app.get("/")
def root():
    return {"message": "Hello Word"}


@app.post("/animais")
def insert_animais(animal: Animais):
    animal.id = str(uuid4())
    banco.append(animal)
    return {"message": f'Animal {animal.nome} Inserido com sucesso'}


@app.get("/animais")
def listar_animais():
    return banco


@app.get("/animais/{id}")
def buscar_animal(id):
    for animal in banco:
        if animal.id == str(id):
            return animal

    return {"message": "animal nao encontrado"}
    
@app.delete("/animais/{id}")
def deletar_animal(id):
    count = 1
    for animal in banco:
        if animal.id == str(id):
            banco.pop(count)
            count +=1
            return {"message": f'Animal {animal.nome} excluido com sucesso'}
            
    return {"message": "animal nao encontrado"}

