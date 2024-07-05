from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from unidecode import unidecode
import csv

def writeCsv(data):
    file = open('carros.csv', 'a+', newline ='')
    with file:    
        write = csv.writer(file)
        write.writerows(data)

def castPreco(preco):
    preco = preco.replace('R$ ', '').replace('.', '')
    
    # Converte para um número inteiro
    preco_int = int(preco)
    
    return preco_int

carros = []

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://rj.olx.com.br/rio-de-janeiro-e-regiao/autos-e-pecas/carros-vans-e-utilitarios/fiat-toro-freedon-1-8-2019-automatica-1315530229?lis=galeria_vitrine"

driver.get(url)

try:
    modelo = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[36]/div/div/div/div[4]/div[2]/div/div[2]/a').text
    marca = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[36]/div/div/div/div[4]/div[3]/div/div[2]/a').text
    ano = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[36]/div/div/div/div[4]/div[5]/div/div[2]/a').text
    direcao = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[36]/div/div/div/div[4]/div[14]/div/div[2]/span[2]').text
    cor = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[36]/div/div/div/div[4]/div[11]/div/div[2]/span[2]').text
    combustivel = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[36]/div/div/div/div[4]/div[8]/div/div[2]/a').text
    tipo = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[36]/div/div/div/div[4]/div[4]/div/div[2]/span[2]').text
    quilometragem = int(driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[36]/div/div/div/div[4]/div[6]/div/div[2]/span[2]').text)
    motor = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[36]/div/div/div/div[4]/div[7]/div/div[2]/span[2]').text
    preco = castPreco(driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[21]/div/div/div/div/div[1]/h2').text)
    regiao = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div/div/div[1]/a').text
    cambio = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[36]/div/div/div/div[4]/div[10]/div/div[2]/span[2]').text
except Exception as e:
        print(f"Erro ao coletar dados do anúncio: {e}")

carro = [modelo, marca, ano, direcao, cor, combustivel, tipo, quilometragem, motor, preco, regiao, cambio]

carro = [item.lower() if isinstance(item, str) else item for item in carro] 
carro = [unidecode(item) if isinstance(item, str) else item for item in carro]
carros.append(carro)

writeCsv(carros)
print(carros)