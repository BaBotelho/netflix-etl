import pandas as pd


def transform():
    # Lê o CSV original baixado da Kaggle
    df = pd.read_csv('data/netflix_titles.csv')

    # Remove linhas sem valor na coluna 'rating'
    df = df.dropna(subset=['rating'])

    # Remove espaços em branco no início/fim de cada valor da coluna 'date_added'
    df['date_added'] = df['date_added'].str.strip()

    # Converte a coluna 'date_added' para formato datetime
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    # Salva os dados limpos em um novo arquivo CSV
    df.to_csv('data/netflix_clean.csv', index=False)

    print("✅ Transformação concluída: arquivo salvo como data/netflix_clean.csv")


if __name__ == '__main__':
    transform()
