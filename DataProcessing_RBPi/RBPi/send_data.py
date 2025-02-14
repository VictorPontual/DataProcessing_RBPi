# Script para enviar os dados ao servidor
import requests
import json
from utils.config import SERVER_URL

def send_data_to_server(data):
    """
    Envia os dados de temperatura e umidade para o servidor FastAPI.
    """
    try:
        response = requests.post(SERVER_URL, json=data)
        if response.status_code == 200:
            print("Dados enviados com sucesso!")
        else:
            print(f"Erro ao enviar dados: {response.status_code}")
    except Exception as e:
        print(f"Erro ao tentar se conectar ao servidor: {e}")
