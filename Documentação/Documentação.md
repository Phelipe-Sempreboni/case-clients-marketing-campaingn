
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

- Apresentação dos dados: Power BI Desktop e Power BI Web.

---

### Ferramentas utilizadas no método de análise II :

- Input dos dados: Microsoft SQL Server 2019.

- Armazenamento dos dados: Microsoft SQL Server 2019.

- Linguagem utilizada para análise dos dados: Python, com bibliotecas como Pandas e api do Power BI.

- Apresentação dos dados: Jupyter Notebook, pela api do Power BI.

---

### Ferramentas utilizadas no método de análise III :

- Input dos dados: Arquivo csv.

- Armazenamento dos dados: Arquivo csv.

- Linguagem utilizada para análise dos dados: Python, com bibliotecas como Pandas e api do Power BI.

- Apresentação dos dados: Jupyter Notebook, pela api do Power BI.

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
