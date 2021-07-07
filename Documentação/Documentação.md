
# Documentação das análises realizadas para o case do Ifood.

---

| Documentação elaborada por     | Tipo | Para  | Data de início | Data de finalização |
| -----------------------------  |:----:|:-----:| :-------------:| :------------------:|
| Luiz Phelipe Utiama Sempreboni | Case | Ifood | 06/07/2021     | Preencher           |


---

### Ferramentas utilizadas no método de análise I :

- Input dos dados: Por meio de job do Python.

- Armazenamento dos dados: Microsoft SQL Server 2019.

- Linguagem utilizada para análise dos dados: Microsoft SQL Server 2019 - (DQL, DML, DDL, DTL), principalmente T-SQL.

- Apresentação dos dados: Power BI Desktop, Power BI Web e Power Point.

---

### Ferramentas utilizadas no método de análise II :

- Input dos dados: Por meio de job do Python.

- Armazenamento dos dados: Microsoft SQL Server 2019.

- Linguagem utilizada para análise dos dados: Python, com bibliotecas como Pandas e api do Power BI.

- Apresentação dos dados: Jupyter Notebook, pela api do Power BI e Power Point.

---

### Ferramentas utilizadas no método de análise III :

- Input dos dados: Arquivo csv.

- Armazenamento dos dados: Arquivo csv.

- Linguagem utilizada para análise dos dados: Python, com bibliotecas como Pandas e api do Power BI.

- Apresentação dos dados: Jupyter Notebook, pela api do Power BI e Power Point.

---

### Observação sobre os métodos de análise I e II :

Os métodos de análise I e II, utilizam o Microsoft SQL Server como banco de dados pelos motivos abaixo: 

- Segurança dos dados: Por exemplo, rastreamento de usuários, tanto nominais, quanto de aplicação, onde é possível verificar qual database, schema ou tabela foi acessado.

- Capacidade de armazenamento dos dados: Por exemplo, uma tabela Excel, ou um arquivo CSV, dependendo da quantidade da dados, pode ocorrer um travamento e até perda dos dados, e já em um banco de dados, com capcidade maior de armazenamento, tem menos riscos de uma ocorrência deste tipo acontecer, e, se for bem gerenciado o banco de dados, teríamos um backup.

- Processamento dos dados: Por exemplo, se a infraestrutura for boa e adequada, o processamento dos dados será mais ágil.

- Backup dos dados: Por exemplo, se o banco for bem gerenciado pelo Administrador ou DBA, com um plano de execução de backups, haverá um backup para restauração dos dados.

Lembrando que, cada análise tem sua peculiaridade, criticidade e tempo de entrega, logo, terá que ser analisado como fazer esse processo de análise com os dados.

---

### Observação sobre o método de análise III :

Notar que para rodar localmente a análise de maneira mais fácil, utilizar o método de análise III, que utiliza diretamente o arquivo csv, que pode ser salvo na área de trabalho e utilizado diretamente no Jupyter Notebook.

---

### Passo a passo do método de análise I :

1º - Ter um usuário e login com privilégios para criação, inserção, drop e delete de databases, schema e tabelas.

2º - Conectar a ferramenta Microsoft SQL Server 2019.

3º - Criar um database que irá alocar o schema e a tabela. O comando abaixo irá criar um database de forma padrão, espelhado no database de sistema chamado (model), pois, não iremos destacar parâmetros neste caso.

```
-- Criação do database.

CREATE DATABASE MARKETING;
GO

-- Caso queira excluir o database criado.

USE master;
GO

DROP DATABASE MARKETING;
GO

```

4º - Criação do schema que alocará a tabela.

```
-- Criação do schema.

USE MARKETING;
GO

CREATE SCHEMA MARKETING_ANALISE_CAMPANHA;
GO

-- Caso queira excluir o schema criado.

USE MARKETING;
GO

DROP SCHEMA MARKETING_ANALISE_CAMPANHA;
GO

```

5º - Criação da tabela que alocará os dados para posteriormente realizar a análise. Nesta etapas, temos alguns passos adicionais conforme explicação abaixo. Esses passos entram como o tratamento de dados antes da realização da análise, para que seja o mais real possível e os dados sejam de qualidade.

- Passos adicionais:

- Essa etapa é realizada em conjunto com o 6º passo do job de importação de dados do Python, pois, como os dados estão sendo importados de diretamente de um arquivo CSV, é necessário verificar os tipos de dados das colunas criadas e se o job consegue realizar a importação dos dados corretamente no banco de dados, sem nenhum erro de tipo de dado incorreto, inválido ou que o mecanismo do banco de dados não consiga realizar a conversão, por exemplo, de (nvarchar) para (numerico), inclusive é um erro que ocorreu e foi corrigido neste passo. Resultado posivito.

- Foi inserido uma chave primária e indíce clusterizado nesta tabela, na coluna ID, pois, por lógica, um ID não se repete em uma tabela, logo, foi inserida chave primária para que o dado não se repita e seja o mais real possível. A chave primária e o indíce clusterizado também deixam as pesquisas na tabela mais ágeis e efetivas. Foi verificado se os 2.240 registros, após a inserção da chave primária se mantinham, e o resultado foi positivo, onde todos os registros foram mantidos.

- Foram confirmados por meios de querys e visando a qualidade dos dados, se os tipos de dados das colunas foram criados corretamente e se a chave primária também foi criada corretamente. Resultado posivito.

- Foram verificados os primeiros 25 registros entre arquivo CSV e tabela criada do banco de dados após a inserção dos dados pelo job do Python, do 6º passo, para garantir por amostras, que os dados estão corretos e assim será para os demais inseridos. Resultado positivo.

- Nesta etapa também foram verificados os valores que estavam vazios no arquivo CSV e feito uma trativa, conforme descrito abaixo:
- Coluna (INCOME): Registros vazios foram preenchidos com (0) e o restante dos registros estavam preenchidos corretamente.

```
-- Criação da tabela.

USE MARKETING;
GO

CREATE TABLE [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA] (
	 ID INT -- Tipo do dado da coluna validado.
	,YEAR_BIRTH INT -- Tipo do dado da coluna validado.
	,EDUCATION VARCHAR (20) -- Tipo do dado da coluna validado.
	,MARITAL_STATUS VARCHAR (20) -- Tipo do dado da coluna validado.
	,INCOME FLOAT -- Tipo do dado da coluna validado.
	,KIDHOME INT -- Tipo do dado da coluna validado.
	,TEENHOME INT -- Tipo do dado da coluna validado.
	,DT_CUSTOMER DATE
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
GO

USE MARKETING;
GO

-- Verificar informações da tabela, onde, a principal verificada neste caso, seria a (COLUMN_NAME) e (DATA_TYPE) para validar os tipos dos dados na criação da tabela.
SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'TBL_DADOS_CAMPANHA';
GO

-- Verificar se informações da tabela, onde, a principal verificada neste caso, seria se a tabela possuí uma chave primária, visando não duplicar registros.
SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS WHERE TABLE_NAME = 'TBL_DADOS_CAMPANHA';
GO

-- Caso queria excluir a tabela criada.

DROP TABLE [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA];
GO

-- Caso queira deletar dados da tabela criada.
DELETE FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA];
GO

- Caso queira truncar dados da tabela criada.
TRUNCA TABLE [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA];
GO
```

6º - Input dos dados na tabela criada no banco de dados Microsoft SQL Server 2019 com um job do Python.

- Atentar para as informações comentadas dentro do script abaixo.

```
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
```
7º - Criação de uma view com algumas adições de novas colunas conforme explicado abaixo.

- A criação da view será feita como se fosse uma boa prática análise de dados em banco de dados, onde temos alguns motivos abaixo.

- Motivo 1: Imaginemos que essa tabela criada seja uma tabela de atualização diária em um Datalake, sendo apagada e recriada todos os dias, logo, se a tabela estiver conectada em alguma ferramenta de visualização, por exemplo, pode causar falhas de atualização da tabela. Criando uma view não teremos esse problema, pois, não temos conexão diretamente na tabela.

- Motivo 2: Caso essa tabela, seja por exemplo, uma tabela de um Datalake, onde normalmente os dados são extraídos e inseridos na base de dados sem tratamentos, podemos criar uma view com nossos próprios tratamentos e não necessitar diretamente da tabela sem tratamentos carregada no Datalake.

- Motivo 3: Na criação da view, podemos adicionar colunas, como colunas calculadas e encapsular esse script caso seja mais restrito.

- Motivo 4: Facilidade de alteração da view, onde caso a tabela não tenha nomes de colunas alteradas, a view sempre será fiel a base origem.

- Motivo 5: Conseguir realizar a transformação de dados sem necessidade de alteração da tabela principal.

- Coluna adicionda: 
- Coluna adicionda: 
- Coluna adicionda: 

```
-- Criação da view.

```

