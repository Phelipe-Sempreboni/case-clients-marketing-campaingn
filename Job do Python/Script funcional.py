# Se não houver instalado, instalar a biblioteca (pyodbc) para realizar a conexão com o banco de dados. Abra o prompt de comando e digite: pip install pyodbc.
# Se não houver instalado, instalar a biblioteca (pandas) para tratar o arquivo CSV. Abra o prompt de comando e digite: pip install pandas.
# Biblioteca (csv) é nativa do Python.

# Importações de bibliotecas.
import pyodbc
import pandas as pd
import csv

# Criação da conexão com o Microsoft SQL Server.
conexao = pyodbc.connect(
Driver='{SQL Server Native Client 11.0}',
Server='', # Insira o server.
Database='', # Insira o banco de dados.
uid='', # Insira o usuário.
pwd='', # Insira a senha.
rusted_Connection='no' # Se o login no banco de dados é realizados com Autentição SQL Server, ou seja, com login e senha, deixe marcado como (no), caso contrário, retire o comando da linha de senha (pwd) e deixe este campo como (yes), informando que a conexão é por meio de Autentição Windows, ou seja, não necessita da senha.
)
cursor = conexao.cursor() # Criação do cursor para executar comandos no banco de dados.

# Dropar/deletar a tabela se ela já existir e recria-lá com os critérios validados.
conexao.execute("""
DROP TABLE IF EXISTS [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA];

CREATE TABLE [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA] (
	 ID INT -- Tipo do dado da coluna validado.
	,YEAR_BIRTH INT -- Tipo do dado da coluna validado.
	,EDUCATION VARCHAR (20) -- Tipo do dado da coluna validado.
	,MARITAL_STATUS VARCHAR (20) -- Tipo do dado da coluna validado.
	,INCOME FLOAT -- Tipo do dado da coluna validado.
	,KIDHOME INT -- Tipo do dado da coluna validado.
	,TEENHOME INT -- Tipo do dado da coluna validado.
	,DT_CUSTOMER DATE -- Tipo do dado da coluna validado.
	,RECENCY INT -- Tipo do dado da coluna validado.
	,MNT_WINES INT -- Tipo do dado da coluna validado.
	,MNT_FRUITS INT -- Tipo do dado da coluna validado.
	,MNT_MEAT_PRODUCTS INT -- Tipo do dado da coluna validado.
	,MNT_FISH_PRODUCTS INT -- Tipo do dado da coluna validado.
	,MNT_SWEET_PRODUCTS INT -- Tipo do dado da coluna validado.
	,MNT_GOLD_PRODS INT -- Tipo do dado da coluna validado.
	,NUM_DEALS_PURCHASES INT -- Tipo do dado da coluna validado.
	,NUM_WEB_PURCHASES INT -- Tipo do dado da coluna validado.
	,NUM_CATALOG_PURCHASES INT -- Tipo do dado da coluna validado.
	,NUM_STORE_PURCHASES INT -- Tipo do dado da coluna validado.
	,NUM_WEB_VISITS_MONTH INT -- Tipo do dado da coluna validado.
	,ACCEPTED_CMP3 INT -- Tipo do dado da coluna validado.
	,ACCEPTED_CMP4 INT -- Tipo do dado da coluna validado.
	,ACCEPTED_CMP5 INT -- Tipo do dado da coluna validado.
	,ACCEPTED_CMP1 INT -- Tipo do dado da coluna validado.
	,ACCEPTED_CMP2 INT -- Tipo do dado da coluna validado.
	,COMPLAIN INT -- Tipo do dado da coluna validado.
	,Z_COST_CONTACT INT -- Tipo do dado da coluna validado.
	,Z_REVENUE INT -- Tipo do dado da coluna validado.
	,RESPONSE INT -- Tipo do dado da coluna validado.
	,CONSTRAINT PK_ID PRIMARY KEY CLUSTERED (ID) -- Chave primária criada para não duplicar dados e facilitar em buscas com índice clusterizado.
);
"""
)

# Manipulação do arquivo CSV.
df = pd.read_csv(r'Desktop\data.csv') # Realizada a leitura.
df.to_csv(r'Desktop\data.csv', header=False, index=False) # Retirado o cabeçalho e possíveis index criados na leitura da linha de comando acima.

# Inserção dos dados do arquivo CSV na tabela criada no banco de dados.
with open(r'Desktop\data.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        to_db = [(row[0]), (row[1]), (row[2]), (row[3]), (row[4]), (row[5]), (row[6]), (row[7]), (row[8]), (row[9]), (row[10]), (row[11]), (row[12]), (row[13]), (row[14]), (row[15]), (row[16]), (row[17]), (row[18]), (row[19]), (row[20]), (row[21]), (row[22]), (row[23]), (row[24]), (row[25]), (row[26]), (row[27]), (row[28])]
        conexao.execute(
        """
        INSERT INTO [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA] (
        ID
        ,YEAR_BIRTH
        ,EDUCATION
        ,MARITAL_STATUS
        ,INCOME
        ,KIDHOME
        ,TEENHOME
        ,DT_CUSTOMER
        ,RECENCY
        ,MNT_WINES
        ,MNT_FRUITS
        ,MNT_MEAT_PRODUCTS
        ,MNT_FISH_PRODUCTS
        ,MNT_SWEET_PRODUCTS
        ,MNT_GOLD_PRODS
        ,NUM_DEALS_PURCHASES
        ,NUM_WEB_PURCHASES
        ,NUM_CATALOG_PURCHASES
        ,NUM_STORE_PURCHASES
        ,NUM_WEB_VISITS_MONTH
        ,ACCEPTED_CMP3
        ,ACCEPTED_CMP4
        ,ACCEPTED_CMP5
        ,ACCEPTED_CMP1
        ,ACCEPTED_CMP2
        ,COMPLAIN
        ,Z_COST_CONTACT
        ,Z_REVENUE
        ,RESPONSE
        ) 
        VALUES 
        (
        ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
        );
        """
        ,to_db
        )
conexao.commit() # Commit para validar e executar as ações.