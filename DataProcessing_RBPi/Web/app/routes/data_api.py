from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import List

router = APIRouter()

class ProcessedData(BaseModel):
    temperature_mean: float
    temperature_stdev: float
    humidity_mean: float
    humidity_stdev: float
    temperature_range: float
    humidity_range: float
    temperature_ls: float
    temperature_li: float
    humidity_ls: float
    humidity_li: float
    temperature_cp: float
    humidity_cp: float
    cpk_temperature: float
    cpk_humidity: float
    ucl_temperature: float
    lcl_temperature: float
    ucl_humidity: float
    lcl_humidity: float
    temperature_outliers: List[float]
    humidity_outliers: List[float]
    temperature_mean_shift: float
    humidity_mean_shift: float
    timestamp: str

received_data = []
active_connections = set()  # Lista de conexões WebSocket ativas

@router.post("/receive_data")
async def receive_data(data: ProcessedData):
    """
    Recebe os dados enviados pelo sensor e os armazena.
    """
    received_data.append(data.model_dump())

    # Enviar os novos dados para todos os clientes WebSocket conectados
    await broadcast_data()

    return {"message": "Dados recebidos com sucesso"}

def get_received_data():
    """ Retorna os dados recebidos """
    return received_data

async def broadcast_data():
    """ Envia os dados atualizados para todos os clientes WebSocket conectados """
    if not received_data:
        return

    data_json = {
        "timestamps": [entry["timestamp"] for entry in received_data],
        "temperature_means": [entry["temperature_mean"] for entry in received_data],
        "humidity_means": [entry["humidity_mean"] for entry in received_data],
        "temperature_stdevs": [entry["temperature_stdev"] for entry in received_data],
        "humidity_stdevs": [entry["humidity_stdev"] for entry in received_data],
        "temperature_ranges": [entry["temperature_range"] for entry in received_data],
        "humidity_ranges": [entry["humidity_range"] for entry in received_data],
        "temperature_lss": [entry["temperature_ls"] for entry in received_data],
        "temperature_lis": [entry["temperature_li"] for entry in received_data],
        "humidity_lss": [entry["humidity_ls"] for entry in received_data],
        "humidity_lis": [entry["humidity_li"] for entry in received_data],
        "temperature_cps": [entry["temperature_cp"] for entry in received_data],
        "humidity_cps": [entry["humidity_cp"] for entry in received_data],
        "cpks_temperature": [entry["cpk_temperature"] for entry in received_data],
        "cpks_humidity": [entry["cpk_humidity"] for entry in received_data],
        "ucls_temperature": [entry["ucl_temperature"] for entry in received_data],
        "lcls_temperature": [entry["lcl_temperature"] for entry in received_data],
        "ucls_humidity": [entry["ucl_humidity"] for entry in received_data],
        "lcls_humidity": [entry["lcl_humidity"] for entry in received_data],
        "temperature_outliers": [entry["temperature_outliers"] for entry in received_data],
        "humidity_outliers": [entry["humidity_outliers"] for entry in received_data],
        "temperature_mean_shift": [entry["temperature_mean_shift"] for entry in received_data],
        "humidity_mean_shift": [entry["humidity_mean_shift"] for entry in received_data],
    }

    for connection in active_connections:
        try:
            await connection.send_json(data_json)
        except:
            active_connections.remove(connection)  # Remove conexões quebradas

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.add(websocket)
    print(f"✅ WebSocket conectado: {websocket.client}")

    try:
        while True:
            await websocket.receive_text()  # Mantém a conexão ativa
    except WebSocketDisconnect:
        active_connections.remove(websocket)
        received_data.clear()
        print(f"❌ WebSocket desconectado: {websocket.client}")
