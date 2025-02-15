# Processamento de estatísticas
import statistics
from sensors.sensor_reader import get_timestamp

def detect_outliers(data, lower_limit, upper_limit):
    """
    Detecta outliers em uma lista de dados utilizando o método do Intervalo Interquartílico (IQR).
    """
    # Identificar outliers: valores fora dos limites inferior e superior
    outliers = [x for x in data if x < lower_limit or x > upper_limit]

    return outliers

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
            "temperature_range": None,
            "humidity_range": None,
            "temperature_ls": None,
            "temperature_li": None,
            "humidity_ls": None,
            "humidity_li": None,
            "temperature_cp": None,
            "humidity_cp": None,
            "cpk_temperature": None,
            "cpk_humidity": None,
            "timestamp": None,
            "ucl_temperature": None,
            "lcl_temperature": None,
            "ucl_humidity": None,
            "lcl_humidity": None,
            "temperature_outliers": None,
            "humidity_outliers": None,
            "temperature_mean_shift": None,
            "humidity_mean_shift": None,
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
        temperature_range = round((max(temperatures) - min(temperatures)), 2)
        humidity_range = round((max(humidities) - min(humidities)), 2)
        temperature_ls = round(max(temperatures), 2)
        temperature_li = round(min(temperatures), 2)
        humidity_ls = round(max(humidities), 2)
        humidity_li = round(min(humidities), 2)
        usl_temperature = round(25.311 + 3*temp_stdev, 2)
        lsl_temperature = round(25.311 - 3*temp_stdev, 2)
        temperature_cp = round((usl_temperature - lsl_temperature) / (6 * temp_stdev), 2)
        usl_humidity = round(51.447 + 3*humidity_stdev, 2)
        lsl_humidity = round(51.447 - 3*humidity_stdev, 2)
        humidity_cp = round((usl_humidity - lsl_humidity) / (6 * humidity_stdev), 2)
        cpk_temperature_upper = round((usl_temperature - temp_mean) / (3 * temp_stdev), 2)
        cpk_temperature_lower = round((temp_mean - lsl_temperature) / (3 * temp_stdev), 2)
        cpk_temperature = round(min(cpk_temperature_upper, cpk_temperature_lower), 2)
        cpk_humidity_upper = round((usl_humidity - humidity_mean) / (3 * humidity_stdev), 2)
        cpk_humidity_lower = round((humidity_mean - lsl_humidity) / (3 * humidity_stdev), 2)
        cpk_humidity = round(min(cpk_humidity_upper, cpk_humidity_lower), 2)
        ucl_temperature = usl_temperature
        lcl_temperature = lsl_temperature
        ucl_humidity = usl_humidity
        lcl_humidity = lsl_humidity
        timestamp = get_timestamp()

        # Detectando outliers com base nos limites
        temperature_outliers = detect_outliers(temperatures, lsl_temperature, usl_temperature)
        humidity_outliers = detect_outliers(humidities, lsl_humidity, usl_humidity)

        # Média esperada (meta)
        expected_temp_mean = 25.0  # Meta para temperatura
        expected_humidity_mean = 50.0  # Meta para umidade

        # Cálculo do deslocamento da média
        temperature_mean_shift = temp_mean - expected_temp_mean
        humidity_mean_shift = humidity_mean - expected_humidity_mean

    except statistics.StatisticsError as e:
        # Em caso de erro no cálculo, como uma lista com um único item
        return {
            "temperature_mean": None,
            "temperature_stdev": None,
            "humidity_mean": None,
            "humidity_stdev": None,
            "temperature_range": None,
            "humidity_range": None,
            "temperature_ls": None,
            "temperature_li": None,
            "humidity_ls": None,
            "humidity_li": None,
            "temperature_cp": None,
            "humidity_cp": None,
            "cpk_temperature": None,
            "cpk_humidity": None,
            "timestamp": None,
            "ucl_temperature": None,
            "lcl_temperature": None,
            "ucl_humidity": None,
            "lcl_humidity": None,
            "temperature_outliers": None,
            "humidity_outliers": None,
            "temperature_mean_shift": None,
            "humidity_mean_shift": None,
        }

    # Retorna as estatísticas calculadas
    return {
        "temperature_mean": temp_mean,
        "temperature_stdev": temp_stdev,
        "humidity_mean": humidity_mean,
        "humidity_stdev": humidity_stdev,
        "temperature_range": temperature_range,
        "humidity_range": humidity_range,
        "temperature_ls": temperature_ls,
        "temperature_li": temperature_li,
        "humidity_ls": humidity_ls,
        "humidity_li": humidity_li,
        "temperature_cp": temperature_cp,
        "humidity_cp": humidity_cp,
        "cpk_temperature": cpk_temperature,
        "cpk_humidity": cpk_humidity,
        "timestamp": timestamp,
        "ucl_temperature": ucl_temperature,
        "lcl_temperature": lcl_temperature,
        "ucl_humidity": ucl_humidity,
        "lcl_humidity": lcl_humidity,
        "temperature_outliers": temperature_outliers,
        "humidity_outliers": humidity_outliers,
        "temperature_mean_shift": temperature_mean_shift,
        "humidity_mean_shift": humidity_mean_shift,
    }