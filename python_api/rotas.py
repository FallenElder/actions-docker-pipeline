from fastapi import FastAPI 
from pydantic import BaseModel
from bd_com import ver_tarefa_bd,criar_tarefa_bd,atualizar_tarefa_bd,apagar_tarefa_bd,criar_tabelas
app = FastAPI() 


class Lista_Tarefa(BaseModel):
    titulo: str
    desc: str
    data: str

@app.get("/tasks/{id}") 
def ver_tarefa(id: int): 
    return ver_tarefa_bd(id)

@app.post("/tasks")
def criar_tarefa(tarefa: Lista_Tarefa):
    criar_tarefa_bd(tarefa.titulo, tarefa.desc, tarefa.data)
    
    return {"mensagem": "Tarefa criada!", "tarefa": tarefa}

@app.put("/tasks/{id}")
def atualizar_tarefa(id: int, tarefa_atualizada: Lista_Tarefa):
    atualizar_tarefa_bd(id, tarefa_atualizada.titulo, tarefa_atualizada.desc, tarefa_atualizada.data)

    return {"mensagem":"Tarefa atualizada", "tarefa":tarefa_atualizada}

@app.delete("/tasks/{id}")
def apagar_tarefa(id: int):
    tarefa_removida = ver_tarefa_bd(id)
    apagar_tarefa_bd(id)

    return {"mensagem":"Tarefa apagada!", "tarefa":tarefa_removida}


@app.on_event("startup")
async def startup_event():
    criar_tabelas()