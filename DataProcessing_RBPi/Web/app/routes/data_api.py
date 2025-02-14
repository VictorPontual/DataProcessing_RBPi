from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import BaseModel

router = APIRouter()

class ProcessedData(BaseModel):
    temperature_mean: float
    temperature_range: float  # Novo campo
    humidity_mean: float
    humidity_range: float  # Novo campo
    temperature_stdev: float
    humidity_stdev: float
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
        "temperature_ranges": [entry["temperature_range"] for entry in received_data],  # Novo campo
        "humidity_means": [entry["humidity_mean"] for entry in received_data],
        "humidity_ranges": [entry["humidity_range"] for entry in received_data],  # Novo campo
        "temperature_stdevs": [entry["temperature_stdev"] for entry in received_data],
        "humidity_stdevs": [entry["humidity_stdev"] for entry in received_data]


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
        print(f"❌ WebSocket desconectado: {websocket.client}")
