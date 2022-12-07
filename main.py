from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from typing import Optional

app = FastAPI()

class ToDo(BaseModel):
    tarefa: str
    realizada: bool
    prazo : Optional[date]


list = [

]


@app.post('/inserir')
def inserir(todo: Todo):
    try:
        list.append(todo)
        return {'status': 'Sucesso!'}

    except:
        return {'status': 'Erro ao inserir'}





