# Script para enviar os dados ao servidor
import os
import csv
import requests
from utils.config import SERVER_URL, DATA_FOLDER
from processing.process_data import process_data

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



def get_sorted_csv_files():
    """
    Obtém a lista de arquivos CSV no diretório de dados, ordenada pelo timestamp no nome do arquivo.
    """
    files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]
    files.sort()  # Ordena alfabeticamente, o que funciona para timestamps no formato YYYYMMDD_HHMMSS
    return files

def read_csv_data(file_path):
    """
    Lê os dados de um arquivo CSV e retorna uma lista de dicionários.
    """
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def send_stored_csv_files():
    """
    Envia os arquivos CSV armazenados para o servidor em ordem cronológica.
    """
    files = get_sorted_csv_files()
    
    for file in files:
        file_path = os.path.join(DATA_FOLDER, file)
        data = read_csv_data(file_path)
        
        if data:  # Verifica se o arquivo não está vazio
            processed_data = process_data(data)
            send_data_to_server(processed_data)