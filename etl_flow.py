# Importando os decoradores de fluxo e tarefa do Prefect
from prefect import flow, task

# Importando nossas funções de ETL feitas anteriormente
from extract import extract
from transform import transform
from load import load

# Transformando as funções em tarefas do Prefect


@task
def t_extract():
    return extract()  # Executa o script extract.py como uma tarefa Prefect


@task
def t_transform():
    return transform()  # Executa o script transform.py como uma tarefa Prefect


@task
def t_load():
    return load()  # Executa o script load.py como uma tarefa Prefect

# Definindo o fluxo (flow) principal de ETL


@flow
def etl_flow():
    t_extract()   # Executa a tarefa de extração
    t_transform()  # Em seguida, transforma os dados
    t_load()      # Por fim, carrega os dados no banco


# Executa o fluxo quando o script for rodado diretamente
if __name__ == '__main__':
    etl_flow()
