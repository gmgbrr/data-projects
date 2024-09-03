import requests
import csv
from datetime import datetime

api_key = '736100546cf24ddf99dc0f73bbac4294'
url = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'
valores_finais = ['date, cpi all items, cpi all less food and energy, cpi gasoline']

# Keys da API
series_ids = [
    'CUSR0000SA0',    # CPI All items
    'CUSR0000SA0L1E', # CPI All items, less food and energy
    'CUSR0000SETB01'  # CPI Gasoline (all types)
]

# Dicionário para armazenar os valores
data_dict = {}

# Função para escrever o .csv
def salvar_csv( data):
    with open('CPI.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for line in data:
            writer.writerow(line.split(', '))

# Função para pegar os valores e adicioná-los no data_dict
def extrair_valores(series_id):
    payload = {
        "seriesid": [series_id],
        "startyear": '2018',
        "endyear": '2024',
        "registrationkey": api_key
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        series_data = data['Results']['series'][0]['data']
        
        for entry in series_data:
            year = entry['year']
            period = entry['period']
            value = entry['value']
            
            if period != "M13":  # Ignorando o valor anual "M13"
                month = int(period[1:])  # Removendo o "M" e convertendo para inteiro
                date_str = f"{month:02}/{year}"
                
                if date_str not in data_dict:
                    data_dict[date_str] = {}
                
                data_dict[date_str][series_id] = value
    else:
        print(f"Erro ao fazer a solicitação: {response.status_code}")

# Extrair valores para todas as keys
for series_id in series_ids:
    extrair_valores(series_id)

# Formatar os objetos e criar uma lista com valores finais
for date_str in sorted(data_dict.keys(), key=lambda x: datetime.strptime(x, "%m/%Y")):
    valores = [date_str]
    for series_id in series_ids:
        valor = data_dict[date_str].get(series_id, "N/A")  # Insere "N/A" se o valor não estiver disponível
        valores.append(valor)
    valores_finais.append(', '.join(valores))

# Exibir os nº de valores
print(f'número de valores: {len(valores_finais)}')

# Salvar os valores em .csv
salvar_csv(valores_finais)