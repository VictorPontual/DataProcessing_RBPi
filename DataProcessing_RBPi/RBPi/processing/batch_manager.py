# Organização dos lotes em arquivos CSV
import csv
import os
from datetime import datetime

def save_to_csv(data, batch_size=10):
    """
    Salva os dados em lotes de CSV. O parâmetro `batch_size` define o número de entradas por lote.
    """
    batch_filename = f"sensor_data_batch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    # Cria o diretório para armazenar os CSVs se não existir
    os.makedirs('data_batches', exist_ok=True)

    # Abre o arquivo CSV para escrita
    with open(f'data_batches/{batch_filename}', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["timestamp", "temperature", "humidity"])
        writer.writeheader()
        
        # Escreve os dados no CSV
        for entry in data:
            writer.writerow(entry)
    
    print(f"Dados salvos em {batch_filename}")