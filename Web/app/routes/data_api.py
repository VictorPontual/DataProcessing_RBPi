from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json

router = APIRouter()

class ProcessedData(BaseModel):
    temperature_mean: float
    temperature_stdev: float
    humidity_mean: float
    humidity_stdev: float
    timestamp: str

# Lista para armazenar temporariamente os dados recebidos (em um cenário real, seria melhor usar um banco de dados)
received_data = []

@router.post("/receive_data")
async def receive_data(data: ProcessedData):
    """
    Recebe dados do sensor de temperatura e umidade da Raspberry Pi.
    """
    # Simula o armazenamento dos dados em uma lista
    received_data.append(data.model_dump())  # Usando o método model_dump()

    # Aqui você pode adicionar lógica para processamento adicional, como salvar em um banco de dados
    # Exemplo de como os dados podem ser processados
    print(f"Recebido: {data.model_dump()}")

    return {"message": "Dados recebidos com sucesso"}

@router.get("/get_received_data")
async def get_received_data():
    """
    Retorna os dados recebidos do sensor.
    """
    if not received_data:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado")
    return {"data": received_data}