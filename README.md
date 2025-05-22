PROYECTO EJEMPLO - MARKDOWN
Crear el entorno
Opción 1: con VsCode
Opción 2: con consola
Agregar las siguientes dependencias en requisitos.txt
Fastapi
uvicornio
pidantico
Ejecutar
pip install -r requisitos.txt
En el archivo main.py ´´´bash from fastapi import FastAPI

aplicación = FastAPI()

@app.get("/") def read_root(): return {"mensaje": "Hola mundo"}

@app.get("/sample/api") def read_sample(): return {"message": "Este es el punto final de la API de muestra"} ´´´

Para ejecutar el servidor:

uvicorn src.main:app --reload