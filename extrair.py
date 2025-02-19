import pandas as pd

caminho_arquivo_original = 'microdados_ed_basica_2023.csv'  
dados = pd.read_csv(caminho_arquivo_original, encoding='latin1', delimiter=';')  

dados_paraiba = dados[dados['NO_UF'] == 'Paraíba'] 
colunas_selecionadas = ['NO_REGIAO', 'NO_UF', 'NO_MUNICIPIO', 'NO_ENTIDADE', 'QT_MAT_BAS', 'QT_MAT_FUND', 'QT_MAT_MED', 'NO_MESORREGIAO', 'NO_MICRORREGIAO' ]
dados_filtrados = dados_paraiba[colunas_selecionadas]

dados_filtrados.columns = ['Regiao', 'UF', 'Municipio', 'Entidade', 'Matriculas Base', 'MAtriculas Fundamental', 'Matriculas Medio', 'Mesoregiao', 'Microregiao']
#caminho_arquivo_filtrado = 'censo_escolar_2023_filtrado.csv'
#dados_filtrados.to_csv(caminho_arquivo_filtrado, index=False, encoding='utf-8', sep=';')
caminho_arquivo_filtrado = 'censo_escolar_2023_filtrado.json'
dados_filtrados.to_json(caminho_arquivo_filtrado, orient='records', lines=True, force_ascii=False)
print(f"Arquivo filtrado salvo com sucesso em: {caminho_arquivo_filtrado}")