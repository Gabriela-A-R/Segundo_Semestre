# %%
# Imports
import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from classes import *

load_dotenv()

# %%
# Conexão com o banco de dados
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")
url = f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(url)

Session = sessionmaker(bind=engine)
session = Session()
# %%
# Consultando a tabela de registros de falha
query = session.query(RegistroFalha)
df = pd.read_sql_query(query.statement, query.session.bind)
print(df)
# %%
# Realizando cálculos e processamentos nos dados
# Calcular a duração da falha
df["duracao"] = df["fim"] - df["inicio"]

# Exibir a contagem de falhas por unidade de produção
falhas_por_unidade = df["numero_unidade_producao"].value_counts()
print(falhas_por_unidade)

# Exibir o tempo total de inatividade severa por unidade de produção
falhas_severas = df[df["severidade"] == True]
tempo_inatividade_severa_por_unidade = falhas_severas.groupby(
    "numero_unidade_producao"
)["duracao"].sum()
print(tempo_inatividade_severa_por_unidade)
# %%