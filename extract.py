# Importa a biblioteca que permite interagir com a API do Kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

# Função responsável por extrair (baixar) os dados


def extract():
    # Cria um objeto da API do Kaggle
    api = KaggleApi()

    # Faz a autenticação com base no arquivo kaggle.json que colocamos em .kaggle/
    api.authenticate()

    # Baixa os arquivos do dataset 'shivamb/netflix-shows' para a pasta 'data/' e descompacta automaticamente
    api.dataset_download_files(
        # ID do dataset no Kaggle (está visível na URL do dataset)
        'shivamb/netflix-shows',
        path='data/',             # Caminho da pasta onde os arquivos serão salvos
        unzip=True                # True = descompacta o arquivo ZIP automaticamente
    )

    # Imprime no terminal que os dados foram baixados com sucesso
    print("✅ Dados baixados em data/")


# Este trecho executa a função extract() se este arquivo for rodado diretamente
if __name__ == '__main__':
    extract()
