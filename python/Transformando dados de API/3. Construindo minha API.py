from fastapi import FastAPI, HTTPException
import csv
import uvicorn
from pathlib import Path

app = FastAPI()

# Converte o .csv para um arquivo .json
def converter_csv(arquivo):
    data = []

    csv_path = Path(arquivo)
    if not csv_path.is_file():
        raise FileNotFoundError(f"O arquivo {arquivo} não foi encontrado.")

    with csv_path.open() as csv_file:
        csv_reader = csv.reader(csv_file)
        field_names = next(csv_reader)

        for row in csv_reader:
            data.append(dict(zip(field_names, row)))

    return data

# Mensagem principal
@app.get("/")
def home():
    return {"message": "API ONLINE", "NÚMERO DE VALORES": len(cpi), 'oioioioi': 'oi'}

# Exibe todos os valores
@app.get("/cpi")
def pegar_cpi():
    return cpi

# Busca um valor por id
@app.get("/cpi/{id_cpi}")
def pegar_cpi(id_cpi: int):
    if id_cpi < 0 or id_cpi >= len(cpi):
        raise HTTPException(status_code=404, detail="ID não encontrado")
    return cpi[id_cpi]

# Exibe um atributo de um id
@app.get("/cpi/{id_cpi}/{atributo}")
def pegar_atributo(id_cpi: int, atributo: str):
    if id_cpi < 0 or id_cpi >= len(cpi):
        raise HTTPException(status_code=404, detail="CPI não encontrado")
    if atributo not in cpi[id_cpi]:
        raise HTTPException(status_code=404, detail="Atributo não encontrado")
    return {atributo: cpi[id_cpi][atributo]}

# Execução
if __name__ == "__main__":
    cpi = converter_csv('CPI.csv')
    uvicorn.run(app, host="127.0.0.1", port=8000)