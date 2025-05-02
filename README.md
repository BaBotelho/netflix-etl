# 🎬 Netflix ETL com Python, Pandas, SQLite e Prefect

Este projeto é um pipeline de ETL (Extract, Transform, Load) utilizando dados da Netflix disponibilizados pela Kaggle. O objetivo é praticar habilidades em Python, engenharia de dados e orquestração de tarefas com Prefect.

---

## 🚀 Tecnologias Utilizadas

- Python 3.12
- Kaggle API
- Pandas
- SQLite
- SQLAlchemy
- Prefect
- VS Code
- Git & GitHub

---

## 🧱 Estrutura do Projeto

```bash
netflix-etl/
│
├── extract.py       # Extração dos dados da Kaggle
├── transform.py     # Limpeza e transformação dos dados com Pandas
├── load.py          # Salvamento dos dados tratados no SQLite
├── etl_flow.py      # Pipeline completo orquestrado com Prefect
├── netflix_titles.csv  # Dataset original
├── netflix.db       # Banco de dados gerado
├── requirements.txt # Bibliotecas utilizadas
└── README.md        # Este arquivo


## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/netflix-etl.git
cd netflix-etl
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuração da Kaggle API

1. Crie uma conta na [Kaggle](https://www.kaggle.com/)
2. Vá até "My Account" e clique em “Create New API Token”
3. Renomeie o arquivo baixado para `kaggle.json` e coloque em `C:\Users\SeuUsuario\.kaggle\` (Windows)
4. Rode:

```bash
kaggle datasets download -d shivamb/netflix-shows
```

---

## 🛠️ Execução do Pipeline

1. Extração:

```bash
python extract.py
```

2. Transformação:

```bash
python transform.py
```

3. Carga no SQLite:

```bash
python load.py
```

4. Orquestração completa com Prefect:

```bash
python etl_flow.py
```

---

## 🧪 Consultando os Dados

Você pode abrir o arquivo `netflix.db` no [DB Browser for SQLite](https://sqlitebrowser.org/) e executar consultas SQL para explorar os dados tratados.

---

## 📌 Observações

* O dataset original está disponível [neste link](https://www.kaggle.com/datasets/shivamb/netflix-shows)
* Este projeto é de fins educacionais para prática de Engenharia de Dados

---

## 👩‍💻 Feito por

**Bárbara Botelho Magalhães [https://www.linkedin.com/in/barbara-botelho-magalhaes/]**
Estudante de Engenharia de Dados com foco em projetos práticos e aprendizado contínuo 🚀

