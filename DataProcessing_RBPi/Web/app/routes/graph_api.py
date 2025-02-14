from fastapi import APIRouter, HTTPException
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")  # Define um backend sem interface gráfica
import io
from fastapi.responses import StreamingResponse
from datetime import datetime
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

    # Extrair dados
    temperature_mean = [data['temperature_mean'] for data in received_data]
    temperature_stdev = [data['temperature_stdev'] for data in received_data]
    humidity_mean = [data['humidity_mean'] for data in received_data]
    humidity_stdev = [data['humidity_stdev'] for data in received_data]

    timestamps = [datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S') for data in received_data]

    # Criar o gráfico
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.set_xlabel('Tempo')
    ax1.set_ylabel('Temperatura Média (°C)', color='tab:red')
    ax1.plot(timestamps, temperature_mean, color='tab:red', label='Temperatura Média')
    ax1.tick_params(axis='y', labelcolor='tab:red')
    ax1.legend(loc='upper left')

    ax1_twin = ax1.twinx()
    ax1_twin.set_ylabel('Umidade Média (%)', color='tab:blue')
    ax1_twin.plot(timestamps, humidity_mean, color='tab:blue', label='Umidade Média')
    ax1_twin.tick_params(axis='y', labelcolor='tab:blue')
    ax1_twin.legend(loc='upper right')

    ax2.set_xlabel('Tempo')
    ax2.set_ylabel('Desvio Padrão da Temperatura (°C)', color='tab:orange')
    ax2.plot(timestamps, temperature_stdev, color='tab:orange', label='Desvio Padrão Temperatura')
    ax2.tick_params(axis='y', labelcolor='tab:orange')
    ax2.legend(loc='upper left')

    ax2_twin = ax2.twinx()
    ax2_twin.set_ylabel('Desvio Padrão da Umidade (%)', color='tab:green')
    ax2_twin.plot(timestamps, humidity_stdev, color='tab:green', label='Desvio Padrão Umidade')
    ax2_twin.tick_params(axis='y', labelcolor='tab:green')
    ax2_twin.legend(loc='upper right')

    plt.xticks(rotation=45)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")
