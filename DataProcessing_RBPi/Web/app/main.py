from fastapi import FastAPI
from fastapi.responses import FileResponse
from .routes import data_api_router, graph_api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite conexões de qualquer origem
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo as rotas no app FastAPI
app.include_router(data_api_router, prefix="/api", tags=["data"])
app.include_router(graph_api_router, prefix="/api", tags=["graph"])

@app.get("/")
async def serve_home():
    return FileResponse("app/static/index.html")