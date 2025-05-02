# Biblioteca para leitura de arquivos e manipulação de dados
import pandas as pd
# Cria a conexão com o banco de dados
from sqlalchemy import create_engine


def load():
    # Cria uma engine de conexão com um banco SQLite chamado netflix.db na pasta data/
    engine = create_engine('sqlite:///data/netflix.db')

    # Lê os dados já transformados no arquivo CSV
    df = pd.read_csv('data/netflix_clean.csv')

    # Carrega os dados para a tabela chamada 'netflix'. Se já existir, substitui.
    df.to_sql('netflix', engine, if_exists='replace', index=False)

    print("✅ Dados carregados com sucesso no banco 'netflix.db', tabela 'netflix'.")


# Executa a função quando rodar o script diretamente
if __name__ == '__main__':
    load()
