import pandas as pd

caminho_arquivo = 'microdados_ed_basica_2023.csv'  
dados = pd.read_csv(caminho_arquivo, encoding='utf-8', delimiter=';', nrows=0)  

colunas = dados.columns.tolist()
print("Colunas disponíveis no arquivo CSV:")
print(len(colunas))