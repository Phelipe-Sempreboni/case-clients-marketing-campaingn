
# Documentação das análises realizadas para o case do Ifood.

---

| Documentação elaborada por     | Tipo | Para  | Data de início | Data de finalização |
| -----------------------------  |:----:|:-----:| :-------------:| :------------------:|
| Luiz Phelipe Utiama Sempreboni | Case | Ifood | 06/07/2021     | Preencher           |


---

### Ferramentas utilizadas no método de análise I :

- Input dos dados: Microsoft SQL Server 2019.

- Armazenamento dos dados: Microsoft SQL Server 2019.

- Linguagem utilizada para análise dos dados: Microsoft SQL Server 2019 - (DQL, DML, DDL, DTL), principalmente T-SQL.

- Apresentação dos dados: Power BI Desktop, Power BI Web e Power Point.

---

### Ferramentas utilizadas no método de análise II :

- Input dos dados: Microsoft SQL Server 2019.

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

5º - Criação da tabela que alocará os dados para posteriormente realizar a análise.

```
```

6º - Input dos dados na tabela no banco de dados Microsoft SQL Server 2019.

- Neste passo, poderíamos utilizar um SSIS, por exemplo, como ferramenta para input dos dados (ETL), ou até um job do Python porém, utilizaremos um procedimento que carregará os dados diretamente os dados do arquivo Excel para a tabela criada que alocará os dados.

- Observação importante deste passo: Caso trabalhe em uma empresa e não seja o administrador do sistema, consulte o DBA (Administrador do banco de dados) para saber se pode ser habilitada está configuração ou se tem algum procedimento para tal, pois, em servidores distribuídos temos a questão da segurança.



