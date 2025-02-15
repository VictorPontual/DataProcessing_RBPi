# Processamento de estatísticas
import statistics
from sensors.sensor_reader import get_timestamp

def process_data(data):
    """
    Processa os dados de temperatura e umidade, retornando a média, desvio padrão e amplitude.
    Se os dados estiverem vazios, retorna None para as estatísticas.
    """
    if not data:
        return {
            "temperature_mean": None,
            "temperature_range": None,
            "humidity_mean": None,
            "humidity_range": None,
            "temperature_stdev": None,
            "humidity_stdev": None,
            "timestamp": None,
            "temp_ls": None,
            "humidity_ls": None,
            "temp_li": None,
            "humidity_li": None,
            "temp_cp" : None,
            "humidity_cp" : None,
            "temp_ck" : None,
            "humidity_ck" : None,
            "temp_resultados": None,
            "humidity_resultados": None

        }

    # Coletando as temperaturas e umidades
    temperatures = [entry['temperature'] for entry in data]
    humidities = [entry['humidity'] for entry in data]

    try:
        # Calculando as médias e desvios padrão
        temp_mean = round(statistics.mean(temperatures), 2)
        temp_stdev = round(statistics.stdev(temperatures), 2) if len(temperatures) > 1 else 0.0
        temp_range = round(max(temperatures) - min(temperatures), 2) if len(temperatures) > 1 else 0.0
        temp_ls = round(temp_mean + 2 * temp_stdev , 2)
        temp_li = round(temp_mean - 2 * temp_stdev , 2)
        temp_cp = round((temp_ls - temp_li)/6*temp_stdev, 2)
        temp_ck = round(min((temp_ls - temp_mean) / 3 * temp_stdev , (temp_mean - temp_li) / 3 * temp_stdev) , 2)
        temp_resultados = ler_e_comparar_csv(temp_ls,temp_li,'temperature')


        humidity_mean = round(statistics.mean(humidities), 2)
        humidity_stdev = round(statistics.stdev(humidities), 2) if len(humidities) > 1 else 0.0
        humidity_range = round(max(humidities) - min(humidities), 2) if len(humidities) > 1 else 0.0
        humidity_ls = round(humidity_mean + 2 * humidity_stdev , 2)
        humidity_li = round(humidity_mean - 2 * humidity_stdev , 2)
        humidity_cp = round((humidity_ls - humidity_li)/6*humidity_stdev, 2)
        humidity_ck = round(min((humidity_ls - humidity_mean) / 3 * humidity_stdev , (humidity_mean - humidity_li) / 3 * humidity_stdev) , 2)
        humidity_resultados = ler_e_comparar_csv(humidity_ls,humidity_li,'humidity')

        
        timestamp = get_timestamp()
    except statistics.StatisticsError:
        # Em caso de erro no cálculo, como uma lista com um único item
        return {
            "temperature_mean": None,
            "temperature_range": None,
            "humidity_mean": None,
            "humidity_range": None,
            "temperature_stdev": None,
            "humidity_stdev": None,
            "timestamp": None,
            "temp_ls": None,
            "humidity_ls": None,
            "temp_li": None,
            "humidity_li": None,
            "temp_cp" : None,
            "humidity_cp" : None,
            "temp_ck" : None,
            "humidity_ck" : None,
            "temp_resultados": None,
            "humidity_resultados": None

        }

    # Retorna as estatísticas calculadas
    return {
        "temperature_mean": temp_mean,
        "temperature_range": temp_range,
        "humidity_mean": humidity_mean,
        "humidity_range": humidity_range,
        "temperature_stdev": temp_stdev,
        "humidity_stdev": humidity_stdev,
        "timestamp": timestamp,
        "temp_ls": temp_ls,
        "humidity_ls": humidity_ls,
        "temp_li": temp_li,
        "humidity_li": humidity_li,
        "temp_cp" : temp_cp,
        "humidity_cp" : humidity_cp,
        "temp_ck" : temp_ck,
        "humidity_ck" : humidity_ck,
        "temp_resultados": temp_resultados,
        "humidity_resultados": humidity_resultados

    }

import os
import csv

def ler_e_comparar_csv(ls, li, type):
    caminho_arquivo = "data_batches"
    
    # Encontrando o arquivo mais recente no diretório
    arquivos = os.listdir(caminho_arquivo)
    arquivos_completo = [os.path.join(caminho_arquivo, arq) for arq in arquivos]
    
    # Pegando o arquivo mais recente
    arquivo_mais_recente = max(arquivos_completo, key=os.path.getmtime)

    # Lendo os dados do arquivo CSV
    data = []
    resultados = []

    with open(arquivo_mais_recente, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(float(row[type]))
    # Comparando os dados com os limites
    for dad in data:
        if not (li <= dad <= ls):
            resultados.append(dad)
    print(resultados)
    return resultados
