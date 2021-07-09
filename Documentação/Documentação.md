
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

### Descrição dos campos da tabela.

### Podemos dizer que são metadados, logo, dados sobre os dados.

| Campo               | Descrição us-es                                                      | Descrição pt-br                                                       |
| :------------------:|---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| AcceptedCmp1        | 1 if costumer accepted the offer in the 1º campaingn, 0 otherwise.   | 1 se o cliente aceitar a oferta na 1ª campanha, 0 caso contrário.     |
| AcceptedCmp2        | 1 if costumer accepted the offer in the 2º campaingn, 0 otherwise.   | 1 se o cliente aceitar a oferta na 2ª campanha, 0 caso contrário.     |
| AcceptedCmp3        | 1 if costumer accepted the offer in the 3º campaingn, 0 otherwise.   | 1 se o cliente aceitar a oferta na 3ª campanha, 0 caso contrário.     |
| AcceptedCmp4        | 1 if costumer accepted the offer in the 4º campaingn, 0 otherwise.   | 1 se o cliente aceitar a oferta na 4ª campanha, 0 caso contrário.     |
| AcceptedCmp5        | 1 if costumer accepted the offer in the 5º campaingn, 0 otherwise.   | 1 se o cliente aceitar a oferta na 5ª campanha, 0 caso contrário.     |
| Response (target)   | 1 if costumer accepted the offer in the last campaingn, 0 otherwise. | 1 se o cliente aceitar a oferta na última campanha, 0 caso contrário. |
| Complain            | 1 if costumer complained in the last 2 years.                        | 1 se o cliente reclamar nos últimos 2 anos.                           |
| DtCustomer          | date of costumer's enrollment with the company.                      | data de inscrição do cliente na empresa.                              |
| Education           | customer's level of education.                                       | nível de educação do cliente.                                         |
| Marital             | customer's marital status.                                           | estado civil do cliente.                                              |
| Kidhome             | number of small children in customer's household.                    | número de crianças pequenas na casa do cliente.                       |
| Teenhome            | number of teenagers in customer's household.                         | número de adolescentes na casa do cliente.                            |
| Income              | customer's yearly household income.                                  | renda familiar anual do cliente.                                      |
| MntFishProducts     | amount spent on fish products in the last 2 yeards.                  | montante gasto em produtos da pesca nos últimos 2 anos.               |
| MntMeatProducts     | amount spent on meat products in the last 2 yeards.                  | montante gasto em produtos cárneos nos últimos 2 anos.                |
| MntFruits           | amount spent on fruits products in the last 2 yeards.                | montante gasto em produtos de frutas nos últimos 2 anos.              |
| MntSweetProducts    | amount spent on sweet products in the last 2 yeards.                 | montante gasto com doces nos últimos 2 anos.                          |
| MntWines            | amount spent on wines products in the last 2 yeards.                 | montante gasto em produtos vitivinícolas nos últimos 2 anos.          |
| MntGoldProds        | amount spent on gold products in the last 2 yeards.                  | montante gasto em produtos de ouro nos últimos 2 anos.                |
| NumDealsPurchases   | number of purchases made with discount.                              | número de compras realizadas com desconto.                            |
| NumCatalogPurchases | number of purchases made using catalogue.                            | número de compras feitas por catálogo.                                |
| NumStorePurchases   | number of purchases made directly in stores.                         | número de compras feitas diretamente nas lojas.                       |
| NumWebPurchases     | number of purchases made through company's web site.                 | número de compras realizadas pelo site da empresa.                    |
| NumWebVisitsMonth   | number of visits to company's web site in the last month.            | número de visitas ao site da empresa no último mês.                   |
| Recency             | number of days since the last purchase.                              | número de dias desde a última compra.                                 |

---

### Passo a passo do método de análise I :

1º - Ter um usuário e login com privilégios para criação, inserção, drop e delete de databases, schema e tabelas.

---

2º - Conectar a ferramenta Microsoft SQL Server 2019.

---

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

---

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

---

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
---

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
```
---

7º - Criação de uma view com algumas adições de novas colunas conforme explicado abaixo.

- A criação da view será feita como se fosse uma boa prática análise de dados em banco de dados, onde temos alguns motivos abaixo.

- Motivo 1: Imaginemos que essa tabela criada seja uma tabela de atualização diária em um Datalake, sendo apagada e recriada todos os dias, logo, se a tabela estiver conectada em alguma ferramenta de visualização, por exemplo, pode causar falhas de atualização da tabela. Criando uma view não teremos esse problema, pois, não temos conexão diretamente na tabela.

- Motivo 2: Caso essa tabela, seja por exemplo, uma tabela de um Datalake, onde normalmente os dados são extraídos e inseridos na base de dados sem tratamentos, podemos criar uma view com nossos próprios tratamentos e não necessitar diretamente da tabela sem tratamentos carregada no Datalake.

- Motivo 3: Na criação da view, podemos adicionar colunas, como colunas calculadas e encapsular esse script caso seja mais restrito.

- Motivo 4: Facilidade de alteração da view, onde caso a tabela não tenha nomes de colunas alteradas, a view sempre será fiel a base origem.

- Motivo 5: Conseguir realizar a transformação de dados sem necessidade de alteração da tabela principal.

#### Colunas adicionadas e descrições:

| Campo                    | Descrição us-es                                                      | Descrição pt-br                                                       |
| :-----------------------:|---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| YEARS OLD                | customer age.                                                        | idade do cliente.                                                     |
| MONTHLY INCOME           | monthly income of the client's family.                               | renda mensal familia do cliente.                                      |
| REGISTERED CUSTOMER TIME | time the customer is registered with the company.                    | tempo que o cliente é registrado na empresa.                          |

```
-- Criação da view.

USE [MARKETING];
GO

CREATE VIEW [MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]
AS
WITH [TBL_DADOS_CAMPANHA_MKT] AS
(
SELECT
       [ID]
      ,[YEAR_BIRTH]
      ,[EDUCATION]
      ,[MARITAL_STATUS]
      ,[INCOME]
      ,[KIDHOME]
      ,[TEENHOME]
      ,[DT_CUSTOMER]
      ,[RECENCY]
      ,[MNT_WINES]
      ,[MNT_FRUITS]
      ,[MNT_MEAT_PRODUCTS]
      ,[MNT_FISH_PRODUCTS]
      ,[MNT_SWEET_PRODUCTS]
      ,[MNT_GOLD_PRODS]
      ,[NUM_DEALS_PURCHASES]
      ,[NUM_WEB_PURCHASES]
      ,[NUM_CATALOG_PURCHASES]
      ,[NUM_STORE_PURCHASES]
      ,[NUM_WEB_VISITS_MONTH]
      ,[COMPLAIN]
      ,[Z_COST_CONTACT]
      ,[Z_REVENUE]
      ,[ACCEPTED_CMP1]
      ,[ACCEPTED_CMP2]
      ,[ACCEPTED_CMP3]
      ,[ACCEPTED_CMP4]
      ,[ACCEPTED_CMP5]
      ,[RESPONSE]
      ,
      CASE
      WHEN [YEAR_BIRTH] NOT IN ('') THEN (YEAR(GETDATE()) - [YEAR_BIRTH])
      WHEN [YEAR_BIRTH] IN ('') THEN 0
      WHEN [YEAR_BIRTH] IN (0) THEN 0
      END AS [YEARS_OLD]
      ,
      CASE
      WHEN [INCOME] NOT IN ('') THEN ROUND(([INCOME] / 12), 0)
      WHEN [INCOME] IN ('') THEN 0
      WHEN [INCOME] IN (0) THEN 0
      END AS [MONTHLY_INCOME]
      ,
      CASE
      WHEN [DT_CUSTOMER] NOT IN ('') THEN (YEAR(GETDATE()) - YEAR([DT_CUSTOMER]))
      END AS [REGISTERED_CUSTOMER_TIME]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA]
),
[TBL_DADOS_CAMPANHA] AS
(
SELECT
      [ID]
     ,[YEAR_BIRTH]
     ,[YEARS_OLD]
     ,[EDUCATION]
     ,[MARITAL_STATUS]
     ,[MONTHLY_INCOME]
     ,[INCOME]
     ,[KIDHOME]
     ,[TEENHOME]
     ,[DT_CUSTOMER]
     ,[REGISTERED_CUSTOMER_TIME]
     ,[RECENCY]
     ,[MNT_WINES]
     ,[MNT_FRUITS]
     ,[MNT_MEAT_PRODUCTS]
     ,[MNT_FISH_PRODUCTS]
     ,[MNT_SWEET_PRODUCTS]
     ,[MNT_GOLD_PRODS]
     ,[NUM_DEALS_PURCHASES]
     ,[NUM_WEB_PURCHASES]
     ,[NUM_CATALOG_PURCHASES]
     ,[NUM_STORE_PURCHASES]
     ,[NUM_WEB_VISITS_MONTH]
     ,[COMPLAIN]
     ,[Z_COST_CONTACT]
     ,[Z_REVENUE]
     ,[ACCEPTED_CMP1]
     ,[ACCEPTED_CMP2]
     ,[ACCEPTED_CMP3]
     ,[ACCEPTED_CMP4]
     ,[ACCEPTED_CMP5]
     ,[RESPONSE]

	  
FROM [TBL_DADOS_CAMPANHA_MKT]
)
SELECT * FROM [TBL_DADOS_CAMPANHA];
GO

-- Caso queira excluir a view.

DROP VIEW [MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW];
GO  
```
---

8º - Levantamento inicial dos KPI's. Nesta etapa, será feito um levantamento inicial dos KPI's que os dados podem nos fornecer.

---
- Quantidade de clientes.
```
SELECT COUNT([ID]) AS [NUMBER_CUSTOMERS] FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW];
GO

-- 2.240 clientes.

```
---
- Idade média dos clientes.
```
SELECT AVG([YEARS_OLD]) AS [AVERAGE_AGE_CUSTOMERS] FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW];
GO

-- 52 anos.
```
---
- Quantidade de clientes pelo nível de educação.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]);

WITH [NUMBER_CUSTOMERS_EDUCATION]
AS
(
SELECT 
      COUNT([ID]) AS [NUMBER_CUSTOMERS]
     ,[EDUCATION]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

GROUP BY
	[EDUCATION]
)
SELECT 
      [NUMBER_CUSTOMERS]
     ,[EDUCATION]
    ,([NUMBER_CUSTOMERS] * 100)/(@NUMBER_CLIENTS) AS [PERCENT]

FROM [NUMBER_CUSTOMERS_EDUCATION]

GROUP BY
       [NUMBER_CUSTOMERS]
      ,[EDUCATION]

-- 1.127 clientes -> Graduation -> 50,3125% -> 50%
-- 486 clientes -> PhD -> 21,696428571428573% -> 21%
-- 370 clientes -> Master -> 16,517857142857142% -> 16%
-- 203 clientes -> 2n Cycle -> 9.0625% -> 9%
-- 54 clientes -> Basic -> 2,4107142857142856% -> 2%
```
---
- Quantidade de clientes pelo estado civil.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]);

WITH [NUMBER_CUSTOMERS_MARITAL_STATUS]
AS
(
SELECT 
      COUNT([ID]) AS [NUMBER_CUSTOMERS]
     ,[MARITAL_STATUS]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

GROUP BY
	[MARITAL_STATUS]
)
SELECT 
      [NUMBER_CUSTOMERS]
     ,[MARITAL_STATUS]
    ,([NUMBER_CUSTOMERS] * 100)/(@NUMBER_CLIENTS) AS [PERCENT]

FROM [NUMBER_CUSTOMERS_MARITAL_STATUS]

GROUP BY
       [NUMBER_CUSTOMERS]
      ,[MARITAL_STATUS]

ORDER BY 
       ([NUMBER_CUSTOMERS] * 100)/(@NUMBER_CLIENTS)

-- 2 clientes -> YOLO -> 0,0892857142857143% -> 1%
-- 3 clientes -> Alone -> 0,1339285714285714% -> 1%
-- 2 clientes -> Absurd -> 0,0892857142857143% -> 1%
-- 77 clientes -> Window -> 3.4375% -> 3%
-- 232 clientes -> Divorced -> 10,357142857142858% -> 10%
-- 480 clientes -> Single -> 21,428571428571427% -> 21%
-- 580 clientes -> Together -> 25,892857142857142% -> 25%
-- 864 clientes -> Married -> 38,57142857142857% -> 38%
```
---
- Quantidade de clientes pelo nível de educação e estado civil.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]);

WITH [NUMBER_CUSTOMERS_EDUCATION_MARITAL_STATUS]
AS
(
SELECT 
      COUNT([ID]) AS [NUMBER_CUSTOMERS]
     ,[EDUCATION]
     ,[MARITAL_STATUS]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

GROUP BY
       [EDUCATION]
      ,[MARITAL_STATUS]
)
SELECT 
      [NUMBER_CUSTOMERS]
     ,[EDUCATION]
     ,[MARITAL_STATUS]
    ,([NUMBER_CUSTOMERS] * 100)/(@NUMBER_CLIENTS) AS [PERCENT]

FROM [NUMBER_CUSTOMERS_EDUCATION_MARITAL_STATUS]

GROUP BY
       [NUMBER_CUSTOMERS]
      ,[EDUCATION]
      ,[MARITAL_STATUS]

ORDER BY 
        [NUMBER_CUSTOMERS]  
       ,([NUMBER_CUSTOMERS] * 100)/(@NUMBER_CLIENTS)
       ,[EDUCATION]
       ,[MARITAL_STATUS]

-- 1 cliente -> Basic -> Divorced -> 0,0446428571428571% -> 1%
-- 1 cliente -> Basic -> Widow -> 0,0446428571428571% -> 1%
-- 1 cliente -> Graduation -> Absurd -> 0,0446428571428571% -> 1%
-- 1 cliente -> Graduation -> Alone -> 0,0446428571428571% -> 1%
-- 1 cliente -> Master -> Absurd -> 0,0446428571428571% -> 1%
-- 1 cliente -> Master -> Alone -> 0,0446428571428571% -> 1%
-- 1 cliente -> PhD -> Alone -> 0,0446428571428571% -> 1%
-- 2 cliente -> PhD -> YOLO -> 0,0892857142857143% -> 1%
-- 5 cliente -> 2n Cycle -> Widow -> 0,2232142857142857% -> 1%
-- 12 cliente -> Master -> Widow -> 0,5357142857142857 -> 1%
-- 14 cliente -> Basic -> Together -> 0,625 -> 1%
-- 18 cliente -> Basic -> Single -> 0,8035714285714286 -> 1%
-- 20 cliente -> Basic -> Married -> 0,8928571428571429 -> 1%
-- 23 cliente -> 2n Cycle -> Divorced -> 0,1034126163391934% -> 1%
-- 24 cliente -> PhD -> Widow -> 1,0714285714285714% -> 1%
-- 35 cliente -> Graduation -> Widow-> 1,5625% -> 1%
-- 37 cliente -> 2n Cycle -> Single -> 1,6517857142857142% -> 1%
-- 37 cliente -> Master -> Divorced -> 1,6517857142857142% -> 1%
-- 52 cliente -> PhD -> Divorced -> 2,3214285714285716% -> 2%
-- 57 cliente -> 2n Cycle -> Together -> 2,544642857142857% -> 2%
-- 75 cliente -> Master -> Single -> 3,3482142857142856% -> 3%
-- 81 cliente -> 2n Cycle -> Married -> 3,6160714285714284% -> 3%
-- 98 cliente -> PhD -> Single -> 4,375% -> 4%
-- 106 cliente -> Master -> Together -> 4,732142857142857% -> 4%
-- 117 cliente -> PhD -> Together -> 5,223214285714286% -> 5%
-- 119 cliente -> Graduation -> Divorced -> 5,3125% -> 5%
-- 138 cliente -> Master -> Married -> 6,160714285714286% -> 6%
-- 192 cliente -> PhD -> Married -> 8,571428571428571% -> 8%
-- 252 cliente -> Graduation -> Single -> 11,25% -> 11%
-- 286 cliente -> Graduation -> Together -> 12,767857142857142% -> 12%
-- 433 cliente -> Graduation -> Married -> 19,330357142857142% -> 19%
```
---
- Renda média mensal familiar dos clientes.
```
SELECT ROUND(AVG([MONTHLY_INCOME]),0) AS [AVERAGE_MONTHLY_INCOME] FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW];
GO

-- 4.307.
```
---
- Renda média anual familiar dos clientes. 
```
SELECT ROUND(AVG([INCOME]),0) AS [AVERAGE_INCOME] FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW];
GO

-- 51.687.
```
---
- Quantitade total de crianças e adoslecentes.
```
SELECT
      SUM([KIDHOME]) AS [NUMBER_KIDHOME]
     ,SUM([TEENHOME]) AS [NUMBER_TEENHOME]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW];

-- 995 crianças.
-- 1.134 adoslecentes.
```
---
- Quantidade de clientes que não possuem crianças e adoslecentes.
- Quantidade de clientes que possuem crianças e adoslecentes.
- Quantidade de clientes que possuem crianças e não adoslecentes.
- Quantidade de clientes que não possuem crianças e possuem adoslecentes.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]);

SELECT
     COUNT([ID]) AS [NUMBER_CUSTOMERS]
    ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
    ,
    CASE
    WHEN COUNT([ID]) NOT IN ('') THEN 'NOT KID AND TEEN'
    END AS [NOTE]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [KIDHOME] IN (0) AND [TEENHOME] IN (0)

UNION ALL

SELECT
     COUNT([ID]) AS [NUMBER_CUSTOMERS]
    ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
    ,
    CASE
    WHEN COUNT([ID]) NOT IN ('') THEN 'YES KID AND TEEN'
    END AS [NOTE]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [KIDHOME] > 0 AND [TEENHOME] > 0

UNION ALL

SELECT
      COUNT([ID]) AS [NUMBER_CUSTOMERS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN 'YES KID AND NOT TEEN'
     END AS [NOTE]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [KIDHOME] > 0 AND [TEENHOME] = 0

UNION ALL

SELECT
      COUNT([ID]) AS [NUMBER_CUSTOMERS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN 'NOT KID AND YES TEEN'
     END AS [NOTE]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [KIDHOME] = 0 AND [TEENHOME] > 0;

-- Não possuem crianças e adoslecentes -> 638 -> 28,482142857142858% -> 28%
-- Possuem crianças e adoslecentes -> 427 -> 19,0625% -> 19%
-- Possuem crianças e não possuem adoslecentes -> 520 -> 23,214285714285715% -> 23%
-- Não possuem crianças e possuem adoslecentes -> 655 -> 29,241071428571427% -> 29%
```
---
- Quantidade de clientes pelo tempo de registro na empresa (em anos).
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]);

SELECT 
      COUNT([ID]) AS [NUMBER_CUSTOMERS]
     ,[REGISTERED_CUSTOMER_TIME]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

GROUP BY
	[REGISTERED_CUSTOMER_TIME]

ORDER BY
	[REGISTERED_CUSTOMER_TIME]

-- 557 clientes -> 7 anos -> 24,866071428571427% -> 24%
-- 1.189 clientes -> 8 anos -> 53,080357142857146 -> 53%
-- 494 clientes -> 9 anos -> 22,053571428571427 -> 22%
```
---
- Média do tempo (em dias) que um cliente passa sem comprar desde a última compra.
```
SELECT AVG([RECENCY]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW];

-- 49 dias.
```
- Produtos mais vendidos e menos vendidos.
```
DECLARE @SUM_GENERAL_PRODUCTS INT = 1356988

WITH [TBL_SUM_PRODUCTS]
AS
(
SELECT 
      SUM([MNT_WINES]) AS [NUMBERS_PRODUCTS]
      ,
      CASE
      WHEN SUM([MNT_WINES]) NOT IN ('') THEN 'MNT_WINES'
      END AS [TYPE_PRODUCT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

UNION ALL

SELECT 
      SUM([MNT_FRUITS]) AS [NUMBERS_PRODUCTS]
     ,
     CASE
     WHEN SUM([MNT_FRUITS]) NOT IN ('') THEN 'MNT_FRUITS'
     END AS [TYPE_PRODUCT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

UNION ALL

SELECT 
      SUM([MNT_MEAT_PRODUCTS]) AS [NUMBERS_PRODUCTS]
     ,
     CASE
     WHEN SUM([MNT_FRUITS]) NOT IN ('') THEN 'MNT_MEAT_PRODUCTS'
     END AS [TYPE_PRODUCT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

UNION ALL

SELECT 
      SUM([MNT_FISH_PRODUCTS]) AS [NUMBERS_PRODUCTS]
     ,
     CASE
     WHEN SUM([MNT_FISH_PRODUCTS]) NOT IN ('') THEN 'MNT_FISH_PRODUCTS'
     END AS [TYPE_PRODUCT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

UNION ALL

SELECT 
      SUM([MNT_SWEET_PRODUCTS]) AS [NUMBERS_PRODUCTS]
      ,
      CASE
      WHEN SUM([MNT_SWEET_PRODUCTS]) NOT IN ('') THEN 'MNT_SWEET_PRODUCTS'
      END AS [TYPE_PRODUCT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

UNION ALL

SELECT 
      SUM([MNT_GOLD_PRODS]) AS [NUMBERS_PRODUCTS]
      ,
      CASE
      WHEN SUM([MNT_GOLD_PRODS]) NOT IN ('') THEN 'MNT_GOLD_PRODS'
      END AS [TYPE_PRODUCT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]
)
SELECT
	  [NUMBERS_PRODUCTS]
	 ,[TYPE_PRODUCT]
	 ,([NUMBERS_PRODUCTS] * 100)/(@SUM_GENERAL_PRODUCTS) AS [PERCENT]

FROM [TBL_SUM_PRODUCTS] ORDER BY [NUMBERS_PRODUCTS];

-- MNT_FRUITS -> 58.917 -> 4,341748047882517 -> 4%
-- MNT_SWEET_PRODUCTS -> 60.621 -> 4,467320271070931 -> 4%
-- MNT_FISH_PRODUCTS -> 84.057 -> 6,19438049562708 -> 6%
-- MNT_GOLD_PRODS -> 98.609 -> 7,26675549083706 -> 7%
-- MNT_MEAT_PRODUCTS -> 373.968 -> 27,558681432702425 -> 27%
-- MNT_WINES -> 680.816 -> 50,171114261879985 -> 50%
```
---
- Quantidade de clientes que compraram com desconto.
- Quantidade de clientes que não usaram ou tiveram desconto.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]);

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN 'bought at a discount'
     END AS [DISCOUNT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_DEALS_PURCHASES] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN 'dont buy with a discount'
     END AS [DISCOUNT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_DEALS_PURCHASES] = 0;

-- 2194 clientes -> 97,94642857142857% -> 97% -> Clientes que compraram com desconto.
-- 46 clientes -> 2,0535714285714284 -> 2% -> Clientes que não usaram ou tiveram desconto
```
---
- Média de compras com desconto.
```
SELECT AVG([NUM_DEALS_PURCHASES]) AS [AVERAGE_NUM_DEALS_PURCHASES] FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW] WHERE [NUM_DEALS_PURCHASES] <> 0;

-- 2.
-- Cada cliente, dos que compraram com desconto, teria uma média de 2 compras por desconto recebido. 
```
---
- Quantidade de clientes pelo número de vezes que ele comprou com desconto.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW] WHERE [NUM_DEALS_PURCHASES] > 0);

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,[NUM_DEALS_PURCHASES]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_DEALS_PURCHASES] > 0

GROUP BY
	[NUM_DEALS_PURCHASES]

ORDER BY
	COUNT([ID])
       ,[NUM_DEALS_PURCHASES] ASC

--  3 clientes -> 13 compras com desconto - Equivalente a (dos 2194 clientes que já compraram com desconto): 0,1367365542388332% -> 1%
--  4 clientes -> 12 compras com desconto - Equivalente a (dos 2194 clientes que já compraram com desconto): 0,1823154056517776% -> 1%
--  5 clientes -> 10 compras com desconto - Equivalente a (dos 2194 clientes que já compraram com desconto): 0,227894257064722%  -> 1%
--  5 clientes -> 11 compras com desconto - Equivalente a (dos 2194 clientes que já compraram com desconto): 0,227894257064722%  -> 1%
--  7 clientes -> 15 compras com desconto - Equivalente a (dos 2194 clientes que já compraram com desconto): 0,3190519598906107% -> 1%
--  8 clientes ->  9 compras com desconto - Equivalente a (dos 2194 clientes que já compraram com desconto): 0,3646308113035551% -> 1%
--  14 clientes -> 8 compras com desconto - Equivalente a (dos 2194 clientes que já compraram com desconto): 0,6381039197812215% -> 1%
--  40 clientes -> 7 compras com desconto - Equivalente a (dos 2194 clientes que já compraram com desconto): 1,8231540565177757% -> 1%
--  61 clientes -> 6 compras com desconto - Equivalente a (dos 2194 clientes que já compraram com desconto): 2,780309936189608% -> 2%
--  94 clientes -> 5 compras com desconto - Equivalente a (dos 2194 clientes que já compraram com desconto): 4,284412032816773% -> 4%
--  189 clientes -> 4 compras com desconto - Equivalente a (dos 2194 clientes que já compraram com desconto): 8,61440291704649% -> 8%
--  297 clientes -> 3 compras com desconto - Equivalente a (dos 2194 clientes que já compraram com desconto): 13,536918869644484% -> 13%
--  497 clientes -> 2 compras com desconto - Equivalente a (dos 2194 clientes que já compraram com desconto): 22,652689152233364% -> 22%
--  970 clientes -> 1 compra com desconto - Equivalente a (dos 2194 clientes que já compraram com desconto): 44,21148587055606% -> 44%
```
---
- Quantidade total de descontos utilizados pelos clientes.
```
SELECT SUM([NUM_DEALS_PURCHASES]) AS [NUM_GENERAL_DEALS_PURCHASES] FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW];

-- 5.208 descontos.
```
---
- Quantidade de clientes que compraram pelo site.
- Quantidade de clientes que não compraram pelo site.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]);

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN 'bought on the site'
     END AS [DISCOUNT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_WEB_PURCHASES] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN 'dont buy on the site'
     END AS [DISCOUNT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_WEB_PURCHASES] = 0;

-- 2191 clientes -> 97,8125% -> 97% -> Clientes que compraram pelo site.
-- 49 clientes -> 2,0081967213114753% -> 2% -> Clientes que não compraram pelo site.
```
---
- Quantidade de clientes pelo número de vezes que ele comprou pelo site.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW] WHERE [NUM_WEB_PURCHASES] > 0);

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,[NUM_WEB_PURCHASES]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_WEB_PURCHASES] > 0

GROUP BY
	[NUM_WEB_PURCHASES]

ORDER BY
	COUNT([ID])
       ,[NUM_WEB_PURCHASES] ASC

--  1 clientes -> 23 compras pelo site - Equivalente a (dos 2191 clientes que já compraram pelo site): 0,0456412596987677% -> 1%
--  1 clientes -> 25 compras pelo site - Equivalente a (dos 2191 clientes que já compraram pelo site): 0,0456412596987677% -> 1%
--  2 clientes -> 23 compras pelo site - Equivalente a (dos 2191 clientes que já compraram pelo site): 0,0912825193975354% -> 1%
--  43 clientes -> 23 compras pelo site - Equivalente a (dos 2191 clientes que já compraram pelo site): 1,9625741670470105% -> 1%
--  44 clientes -> 23 compras pelo site - Equivalente a (dos 2191 clientes que já compraram pelo site): 2,008215426745778% -> 2%
--  75 clientes -> 23 compras pelo site - Equivalente a (dos 2191 clientes que já compraram pelo site): 3,4230944774075764% -> 3%
--  102 clientes -> 23 compras pelo site - Equivalente a (dos 2191 clientes que já compraram pelo site): 4,655408489274304% -> 4%
--  155 clientes -> 23 compras pelo site - Equivalente a (dos 2191 clientes que já compraram pelo site): 7,0743952533089915% -> 7%
--  205 clientes -> 23 compras pelo site - Equivalente a (dos 2191 clientes que já compraram pelo site): 9,356458238247376% -> 9%
--  220 clientes -> 23 compras pelo site - Equivalente a (dos 2191 clientes que já compraram pelo site): 10,04107713372889% -> 10%
--  280 clientes -> 23 compras pelo site - Equivalente a (dos 2191 clientes que já compraram pelo site): 12,779552715654953% -> 12%
--  336 clientes -> 23 compras pelo site - Equivalente a (dos 2191 clientes que já compraram pelo site): 15,335463258785943% -> 15%
--  354 clientes -> 23 compras pelo site - Equivalente a (dos 2191 clientes que já compraram pelo site): 16,15700593336376% -> 16%
--  373 clientes -> 23 compras pelo site - Equivalente a (dos 2191 clientes que já compraram pelo site): 17,024189867640345% -> 17%
```
---
- Quantidade total de compras pelo site.
```
SELECT SUM([NUM_WEB_PURCHASES]) AS [NUM_GENERAL_WEB_PURCHASES] FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW];

-- 9.150 de compras pelo site.
```
---
- Quantidade de clientes que compraram pelo catálogo.
- Quantidade de clientes que não compraram pelo catálogo.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]);

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN 'bought from the catalog.'
     END AS [DISCOUNT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_CATALOG_PURCHASES] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN 'they dont buy from the catalog.'
     END AS [DISCOUNT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_CATALOG_PURCHASES] = 0;

-- 1654 clientes -> 73,83928571428571% -> 73% -> Clientes que compraram pelo catálogo.
-- 586 clientes -> 26,160714285714285% -> 26% -> Clientes que não compraram pelo catálogo.
```
---
- Quantidade de clientes pelo número de vezes que ele comprou pelo catálogo.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW] WHERE [NUM_CATALOG_PURCHASES] > 0);

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,[NUM_CATALOG_PURCHASES]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_CATALOG_PURCHASES] > 0

GROUP BY
	[NUM_CATALOG_PURCHASES]

ORDER BY
	COUNT([ID])
       ,[NUM_CATALOG_PURCHASES] ASC

--  1 clientes -> 22 compras pelo catálogo - Equivalente a (dos 1654 clientes que já compraram pelo catálogo): 0,060459492140266% -> 1%
--  3 clientes -> 28 compras pelo catálogo - Equivalente a (dos 1654 clientes que já compraram pelo catálogo): 0,1813784764207981% -> 1%
--  19 clientes -> 11 compras pelo catálogo - Equivalente a (dos 1654 clientes que já compraram pelo catálogo): 1,1487303506650544% -> 1%
--  42 clientes -> 9 compras pelo catálogo - Equivalente a (dos 1654 clientes que já compraram pelo catálogo): 2,539298669891173% -> 2%
--  48 clientes -> 10 compras pelo catálogo - Equivalente a (dos 1654 clientes que já compraram pelo catálogo): 2,902055622732769% -> 2%
--  55 clientes -> 8 compras pelo catálogo - Equivalente a (dos 1654 clientes que já compraram pelo catálogo): 3,3252720677146312% -> 3%
--  79 clientes -> 7 compras pelo catálogo - Equivalente a (dos 1654 clientes que já compraram pelo catálogo): 4,776299879081016% -> 4%
--  128 clientes -> 6 compras pelo catálogo - Equivalente a (dos 1654 clientes que já compraram pelo catálogo): 7,738814993954051% -> 7%
--  140 clientes -> 5 compras pelo catálogo - Equivalente a (dos 1654 clientes que já compraram pelo catálogo): 8,464328899637243% -> 8%
--  182 clientes -> 4 compras pelo catálogo - Equivalente a (dos 1654 clientes que já compraram pelo catálogo): 11,003627569528415% -> 11%
--  184 clientes -> 3 compras pelo catálogo - Equivalente a (dos 1654 clientes que já compraram pelo catálogo): 11,124546553808948% -> 11%
--  276 clientes -> 2 compras pelo catálogo - Equivalente a (dos 1654 clientes que já compraram pelo catálogo): 16,68681983071342% -> 16%
--  497 clientes -> 1 compras pelo catálogo - Equivalente a (dos 1654 clientes que já compraram pelo catálogo): 30,048367593712214% -> 30%
```
---
- Quantidade total de compras pelo catálogo.
```
SELECT SUM([NUM_CATALOG_PURCHASES]) AS [NUM_GENERAL_CATALOG_PURCHASES] FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW];

-- 5.963 compras pelo catálogo.
```
---
- Quantidade de clientes que compraram na loja.
- Quantidade de clientes que não compraram na loja.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]);

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN 'bought by the store.'
     END AS [DISCOUNT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_STORE_PURCHASES] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN 'not bought by the store.'
     END AS [DISCOUNT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_STORE_PURCHASES] = 0;

-- 2225 clientes -> 99,33035714285714% -> 99% -> Clientes que compraram na loja.
-- 15 clientes -> 0,6696428571428571% -> 1% -> Clientes que não compraram na loja.
```
---
- Quantidade de clientes pelo número de vezes que ele comprou na loja.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW] WHERE [NUM_STORE_PURCHASES] > 0);

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,[NUM_STORE_PURCHASES]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_STORE_PURCHASES] > 0

GROUP BY
	[NUM_STORE_PURCHASES]

ORDER BY
	COUNT([ID])
       ,[NUM_STORE_PURCHASES] ASC

--  7 clientes -> 1 compras pela loja - Equivalente a (dos 2225 clientes que já compraram pela loja): 0,3146067415730337% -> 1%
--  81 clientes -> 11 compras pela loja - Equivalente a (dos 2225 clientes que já compraram pela loja): 3,640449438202247% -> 3%
--  83 clientes -> 13 compras pela loja - Equivalente a (dos 2225 clientes que já compraram pela loja): 3,730337078651685% -> 3%
--  105 clientes -> 12 compras pela loja - Equivalente a (dos 2225 clientes que já compraram pela loja): 4,719101123595506% -> 4%
--  106 clientes -> 9 compras pela loja - Equivalente a (dos 2225 clientes que já compraram pela loja): 4,764044943820225% -> 4%
--  125 clientes -> 10 compras pela loja - Equivalente a (dos 2225 clientes que já compraram pela loja): 5,617977528089888% -> 5%
--  143 clientes -> 7 compras pela loja - Equivalente a (dos 2225 clientes que já compraram pela loja): 6,426966292134831% -> 6%
--  149 clientes -> 8 compras pela loja - Equivalente a (dos 2225 clientes que já compraram pela loja): 6,696629213483146% -> 6%
--  178 clientes -> 6 compras pela loja - Equivalente a (dos 2225 clientes que já compraram pela loja): 8% -> 8%
--  212 clientes -> 5 compras pela loja - Equivalente a (dos 2225 clientes que já compraram pela loja): 9,52808988764045% -> 9%
--  223 clientes -> 2 compras pela loja - Equivalente a (dos 2225 clientes que já compraram pela loja): 10,02247191011236% -> 10%
--  323 clientes -> 4 compras pela loja - Equivalente a (dos 2225 clientes que já compraram pela loja): 14,51685393258427% -> 14%
--  490 clientes -> 3 compras pela loja - Equivalente a (dos 2225 clientes que já compraram pela loja): 22,02247191011236% -> 22%
```
---
- Quantidade total de compras na loja.
```
SELECT SUM([NUM_STORE_PURCHASES]) AS [NUM_GENERAL_STORE_PURCHASES] FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW];

-- 12.970 de compras pela loja.
```
--
- Quantidade de clientes que visitaram o site no último mês.
- Quantidade de clientes que não visitaram o site no último mês.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]);

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN 'visited the site in the last month.'
     END AS [DISCOUNT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_WEB_VISITS_MONTH] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN 'dont visited the site in the last month.'
     END AS [DISCOUNT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_WEB_VISITS_MONTH] = 0;

-- 2229 clientes -> 99,50892857142857% -> 99% -> Clientes que visitaram o site da loja no último mês.
-- 11 clientes -> 0,4910714285714285% -> 1% -> Clientes que não visitaram o site da loja no último mês.
```
---
- Quantidade de clientes pelo número de vezes visitaram o site no último mês.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW] WHERE [NUM_WEB_VISITS_MONTH] > 0);

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,[NUM_WEB_VISITS_MONTH]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]

FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [NUM_WEB_VISITS_MONTH] > 0

GROUP BY
	[NUM_WEB_VISITS_MONTH]

ORDER BY
	COUNT([ID])
   ,[NUM_WEB_VISITS_MONTH] ASC

--  1 clientes -> 13 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 0,0448631673396142% -> 1%
--  1 clientes -> 17 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 0,0448631673396142% -> 1%
--  2 clientes -> 14 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 0,0897263346792284% -> 1%
--  2 clientes -> 19 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 0,0897263346792284% -> 1%
--  3 clientes -> 10 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 0,1345895020188425% -> 1%
--  3 clientes -> 20 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 0,1345895020188425% -> 1%
--  83 clientes -> 9 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 3,7236428891879765% -> 3%
--  153 clientes -> 1 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 6,864064602960969% -> 6%
--  202 clientes -> 2 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 9,062359802602064% -> 9%
--  205 clientes -> 3 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 9,196949304620906% -> 9%
--  218 clientes -> 4 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 9,78017048003589% -> 9%
--  281 clientes -> 5 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 12,606550022431584% -> 12%
--  340 clientes -> 6 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 15,25347689546882% -> 15%
--  342 clientes -> 8 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 15,343203230148049% -> 15%
--  393 clientes -> 7 visitas no site no último mês - Equivalente a (dos 2229 clientes que visitaram o site no último mês): 17,63122476446837% -> 17%
```
---
- Quantidade total de visitas no site no último mês.
```
SELECT SUM([NUM_WEB_VISITS_MONTH]) AS [NUM_GENERAL_WEB_VISITS_MONTH] FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW];

-- 11.909 de visitas no site no último mês.
```
---
- Quantidade de clientes que aceitaram e não aceitaram a oferta na 1º campanha.
- Quantidade de clientes que aceitaram e não aceitaram a oferta na 2º campanha.
- Quantidade de clientes que aceitaram e não aceitaram a oferta na 3º campanha.
- Quantidade de clientes que aceitaram e não aceitaram a oferta na 4º campanha.
- Quantidade de clientes que aceitaram e não aceitaram a oferta na 5º campanha.
- Quantidade de clientes que aceitaram e não aceitaram a oferta na 6º campanha.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]);

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
    ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
    ,
    CASE
    WHEN COUNT([ID]) NOT IN ('') THEN '1º - CLIENTS NOT ACCEPTED CMP1'
    END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP1] = 0

UNION ALL 

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '1º - CLIENTS ACCEPTED CMP1'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP1] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '2º - CLIENTS NOT ACCEPTED CMP2'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP2] = 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
    ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
    ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '2º - CLIENTS ACCEPTED CMP2'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP2] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '3º - CLIENTS NOT ACCEPTED CMP3'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP3] = 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '3º - CLIENTS ACCEPTED CMP3'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP3] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '4º - CLIENTS NOT ACCEPTED CMP4'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP4] = 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '4º - CLIENTS ACCEPTED CMP4'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP4] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '5º - CLIENTS NOT ACCEPTED CMP5'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP5] = 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '5º - CLIENTS ACCEPTED CMP5'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP5] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '6º - CLIENTS NOT ACCEPTED (RESPONSE - TARGET)'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [RESPONSE] = 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
     ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '6º - CLIENTS ACCEPTED (RESPONSE - TARGET)'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [RESPONSE] > 0

-- 1º Campanha:
-- 2096 -> 93,57142857142857% -> 93% -> Clientes que não aceitaram a oferta na 1º campanha.
-- 144 -> 6,428571428571429% -> 6% -> Clientes que aceitaram a oferta na 1º campanha.

-- 2º Campanha:
-- 2096 -> 98,66071428571429% -> 98% -> Clientes que não aceitaram a oferta na 2º campanha.
-- 30 -> 1,3392857142857142% -> 1% -> Clientes que aceitaram a oferta na 2º campanha.

-- 3º Campanha:
-- 2077 -> 92,72321428571429% -> 92% -> Clientes que não aceitaram a oferta na 3º campanha.
-- 163 -> 7,276785714285714% -> 7% -> Clientes que aceitaram a oferta na 3º campanha.

-- 4º Campanha:
-- 2073 -> 92,54464285714286% -> 92% -> Clientes que não aceitaram a oferta na 4º campanha.
-- 167 -> 7,455357142857143% -> 7% -> Clientes que aceitaram a oferta na 4º campanha.

-- 5º Campanha:
-- 2077 -> 92,72321428571429% -> 92% -> Clientes que não aceitaram a oferta na 5º campanha.
-- 163 -> 7,276785714285714% -> 7% -> Clientes que aceitaram a oferta na 5º campanha.

-- 6º Campanha (Última):
-- 1906 -> 85,08928571428571% -> 85% -> Clientes que não aceitaram a oferta na 6º Campanha (última).
-- 334 -> 14,910714285714286% -> 14% -> Clientes que aceitaram a oferta na 6º Campanha (última).
```
---
- Média de sucesso da campanha.
```
DECLARE @NUMBER_CLIENTS INT = (SELECT COUNT([ID]) FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]);

WITH [TBL_ACCEPTED_NOT_ACCEPTED_CMPS_RESPONSE] AS
(
SELECT 
	  COUNT([ID]) AS [NUMBER_CLIENTS]
	 ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
	 ,
	 CASE
	 WHEN COUNT([ID]) NOT IN ('') THEN '1º - CLIENTS NOT ACCEPTED CMP1'
	 END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP1] = 0

UNION ALL 

SELECT 
	  COUNT([ID]) AS [NUMBER_CLIENTS]
	 ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
	 ,
	 CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '1º - CLIENTS ACCEPTED CMP1'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP1] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
	 ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '2º - CLIENTS NOT ACCEPTED CMP2'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP2] = 0

UNION ALL

SELECT 
	  COUNT([ID]) AS [NUMBER_CLIENTS]
	 ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
	 ,
	 CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '2º - CLIENTS ACCEPTED CMP2'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP2] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
	 ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '3º - CLIENTS NOT ACCEPTED CMP3'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP3] = 0

UNION ALL

SELECT 
	  COUNT([ID]) AS [NUMBER_CLIENTS]
	 ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
	 ,
	 CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '3º - CLIENTS ACCEPTED CMP3'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP3] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
	 ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '4º - CLIENTS NOT ACCEPTED CMP4'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP4] = 0

UNION ALL

SELECT 
	  COUNT([ID]) AS [NUMBER_CLIENTS]
	 ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
	 ,
	 CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '4º - CLIENTS ACCEPTED CMP4'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP4] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
	 ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '5º - CLIENTS NOT ACCEPTED CMP5'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP5] = 0

UNION ALL

SELECT 
	  COUNT([ID]) AS [NUMBER_CLIENTS]
	 ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
	 ,
	 CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '5º - CLIENTS ACCEPTED CMP5'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [ACCEPTED_CMP5] > 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
	 ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '6º - CLIENTS NOT ACCEPTED (RESPONSE - TARGET)'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [RESPONSE] = 0

UNION ALL

SELECT 
      COUNT([ID]) AS [NUMBER_CLIENTS]
	 ,(COUNT([ID]) * 100)/(@NUMBER_CLIENTS) AS [PERCENT]
     ,
     CASE
     WHEN COUNT([ID]) NOT IN ('') THEN '6º - CLIENTS ACCEPTED (RESPONSE - TARGET)'
     END AS [RESPONSE]
	  
FROM [MARKETING].[MARKETING_ANALISE_CAMPANHA].[TBL_DADOS_CAMPANHA_VW]

WHERE [RESPONSE] > 0
)
SELECT 
	  AVG([PERCENT]) AS [AVG_PERCENT_SUCESS_CAMPAIGN]

FROM [TBL_ACCEPTED_NOT_ACCEPTED_CMPS_RESPONSE]

WHERE [RESPONSE] LIKE '%CLIENTS ACCEPTED%'

-- Média de sucesso da campanha.
-- Analisando da primeira a última campanha, temos uma média de sucesso de 7%.
```
---



