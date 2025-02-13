# Processamento de estatísticas
import statistics
from sensors.sensor_reader import get_timestamp

def process_data(data):
    """
    Processa os dados de temperatura e umidade, retornando a média e o desvio padrão.
    Se os dados estiverem vazios, retorna None para as estatísticas.
    """
    if not data:
        return {
            "temperature_mean": None,
            "temperature_stdev": None,
            "humidity_mean": None,
            "humidity_stdev": None,
            "timestamp": None
        }

    # Coletando as temperaturas e umidades
    temperatures = [entry['temperature'] for entry in data]
    humidities = [entry['humidity'] for entry in data]

    try:
        # Calculando as médias e desvios padrão
        temp_mean = round(statistics.mean(temperatures), 2)
        temp_stdev = round(statistics.stdev(temperatures), 2) if len(temperatures) > 1 else 0.0
        humidity_mean = round(statistics.mean(humidities), 2)
        humidity_stdev = round(statistics.stdev(humidities), 2) if len(humidities) > 1 else 0.0
        timestamp = get_timestamp()
    except statistics.StatisticsError as e:
        # Em caso de erro no cálculo, como uma lista com um único item
        return {
            "temperature_mean": None,
            "temperature_stdev": None,
            "humidity_mean": None,
            "humidity_stdev": None,
            "timestamp": None
        }

    # Retorna as estatísticas calculadas
    return {
        "temperature_mean": temp_mean,
        "temperature_stdev": temp_stdev,
        "humidity_mean": humidity_mean,
        "humidity_stdev": humidity_stdev,
        "timestamp": timestamp
    }