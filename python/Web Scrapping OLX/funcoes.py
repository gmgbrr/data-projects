from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from unidecode import unidecode
import funcoes
import csv

#escreve os dados do scrapping dentro do csv
def writeCsv(data):
    file = open('carros.csv', 'a+', newline ='')
    with file:    
        write = csv.writer(file)
        write.writerows(data)


#limpa a string de preco e converte para int
def castPreco(preco):
    preco = preco.replace('R$ ', '').replace('.', '')
    
    # Converte para um número inteiro
    preco_int = int(preco)
    
    return preco_int


#Scrapping da página
def pageScrapping(url, driver):

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
        preco = funcoes.castPreco(driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[21]/div/div/div/div/div[1]/h2').text)
        regiao = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div/div/div[1]/a').text
        cambio = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[2]/div[1]/div[36]/div/div/div/div[4]/div[10]/div/div[2]/span[2]').text
    except Exception as e:
            print(f"Erro ao coletar dados do anúncio: {e}")

    valores = [modelo, marca, ano, direcao, cor, combustivel, tipo, quilometragem, motor, preco, regiao, cambio]

    return valores