# Script principal que gerencia a coleta e envio dos dados
import time
from sensors.mock_sensor import simulate_sensor_reading
from processing.batch_manager import save_to_csv
from processing.process_data import process_data
from send_data import send_data_to_server
from utils.config import BATCH_SIZE, READ_INTERVAL

def main():
    """
    Função principal que gerencia a coleta, processamento e envio de dados.
    """
    data_batch = []

    while True:
        # Simula a leitura dos sensores
        sensor_data = simulate_sensor_reading()
        
        # Adiciona os dados ao lote
        data_batch.append(sensor_data)
        
        # Se o número de leituras atingir o limite do lote, salva os dados e envia
        if len(data_batch) >= BATCH_SIZE:
            # Processa os dados do lote
            processed_data = process_data(data_batch)
            print(f"Dados processados: {processed_data}")

            # Envia os dados para o servidor
            send_data_to_server(processed_data)

            # Salva os dados em um arquivo CSV
            save_to_csv(data_batch)

            # Limpa o lote de dados
            data_batch = []
        
        # Aguarda o próximo intervalo de leitura
        time.sleep(READ_INTERVAL)

if __name__ == "__main__":
    main()
