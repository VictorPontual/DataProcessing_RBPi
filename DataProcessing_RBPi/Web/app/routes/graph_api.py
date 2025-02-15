from fastapi import APIRouter, HTTPException
import matplotlib
matplotlib.use("Agg")  # Define um backend sem interface gráfica
from .data_api import get_received_data  # Agora importa a função, não a variável direta

router = APIRouter()

@router.get("/graph")
async def generate_graph():
    """
    Gera gráficos a partir dos dados recebidos.
    """
    received_data = get_received_data()  # Obtém os dados da função

    if not received_data:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado para gerar gráfico")

   
