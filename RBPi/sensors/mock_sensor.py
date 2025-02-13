# Simulação do sensor para testes
from .sensor_reader import read_sensor, get_timestamp

def simulate_sensor_reading():
    """
    Simula a leitura de dados do sensor de temperatura e umidade.
    """
    temperature, humidity = read_sensor()
    timestamp = get_timestamp()
    
    return {
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": timestamp
    }
