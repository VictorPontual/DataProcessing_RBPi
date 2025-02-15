# Código para capturar os dados do sensor
import random
import time
import numpy as np


def read_sensor():
    """
    Simula a leitura de um sensor de temperatura e umidade.
    Em um cenário real, você substituiria isso por código para
    interagir com o hardware do sensor.
    """
    temperature = round(np.random.normal(25.0, 1.5), 2)  # Temperatura simulada entre 20.0 e 30.0°C
    humidity = round(np.random.normal(50.0, 5.0), 2)     # Umidade simulada entre 40% e 60%
    
    return temperature, humidity

def get_timestamp():
    """
    Retorna o timestamp atual.
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
