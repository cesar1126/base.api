from typing import Dict
from fastapi import FastAPI # type: ignore
from message_services import MessageService

app = FastAPI()

my_servicio = MessageService

@app.get("/")
def read_root():
    return {"message": "hello world"}

@app.post("/api/message")
def send_message(message: Dict):
    my_servicio.add_message(message)
    return {"Message": "message received"}  

@app.get("/api/message")
def read_message():
    return my_servicio.get_messages()

@app.put("/api/message/{id}")
def update_message(id: int, message: Dict):
    my_servicio.update_message(id, message)
    

