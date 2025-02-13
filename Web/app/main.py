from fastapi import FastAPI
from .routes import data_api_router, graph_api_router

app = FastAPI()

# Incluindo as rotas no app FastAPI
app.include_router(data_api_router, prefix="/api", tags=["data"])
app.include_router(graph_api_router, prefix="/api", tags=["graph"])

@app.get("/")
def read_root():
    return {"message": "Servidor está rodando!"}