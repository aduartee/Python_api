from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from typing import Optional

app = FastAPI()

class ToDo(BaseModel):
    tarefa: str
    realizada: bool
    prazo : Optional[date]


lista = [

]


@app.post('/inserir')
def inserir(todo: ToDo):
    try:
        list.append(todo)
        return {'status': 'Sucesso!'}

    except:
        return {'status': 'Erro ao inserir'}



@app.post('/listar')
def listar(opcao : int = 0):
    if opcao == 0:
        return lista
    elif opcao == 1:
        return list(filter(lambda x: x.realizada == False, lista))

    elif opcao == 2:
        return list(filter(lambda x: x.realizada == True, lista))


@app.get('/listaunica/{id}')
def listar(id : int):
    try:
        return lista[id]

    except:
        return {'status': 'Error'}

@app.post('/alteraStatus')
def altera(id : int):
    try:
        lista[id].realizada = not lista[id].realizada
        return {'status' : 'Operação realizada' }
    except:
        return {'status' : 'Error'}

@app.post('/Excluir')
def excluir(id : int):
    try:
        del lista[id]
        return {'status': 'Operação realizada'}

    except:
        return {'id' : 'Error'}




