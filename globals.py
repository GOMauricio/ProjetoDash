import pandas as pd
import os

# Identificar, com o pandas, as planilhas e permitir leitura das mesmas
if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)

# Ocasionalmente, os dados armazenados em Pandas podem fugir do padrão deles (no caso da data, que foi arquivada como objeto)
# Para isso, se usa a conversão to_datetime para transformar o mesmo em data e o lambda para deixar na formatação ideal
# Permitindo que os dados possam ser facilmente manipulados 
    df_receitas['Data'] = pd.to_datetime(df_receitas['Data'])
    df_despesas['Data'] = pd.to_datetime(df_despesas['Data'])
    df_receitas = df_receitas['Data'].apply(lambda x: x.date())
    df_despesas = df_despesas['Data'].apply(lambda x: x.date())

# Caso o diretório/arquivo não exista, ele será criado seguindo a estrutura estabelecida na data_structure.
else:
    data_structure = {'Valor': [],
                        'Efetuado': [],
                        'Fixo': [],
                        'Data': [],
                        'Categoria': [],
                        'Descrição': [],}
    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_despesas.to_csv("df_despesas.csv")
    df_receitas.to_csv("df_receitas.csv")

# Busca e criação dos docs que salvam as categorias de receitas/despesas
if ("df_cat_despesa.csv" in os.listdir()) and ("df_cat_receita.csv" in os.listdir()):
    df_cat_despesa = pd.read_csv("df_cat_despesa.csv", index_col=0, parse_dates=True)
    df_cat_receita = pd.read_csv("df_cat_receita.csv", index_col=0, parse_dates=True)
    cat_receita = df_cat_receita.values.tolist()
    cat_despesa = df_cat_despesa.values.tolist()

# Caso o diretório/arquivo não exista, ele será criado seguindo a estrutura estabelecida na data_structure.
else:
    cat_receita = {'Categoria': ["Salário", "Investimentos", "Comissão"]}
    cat_despesas = {'Categoria': ["Alimentação", "Aluguel", "Lazer", "Contas"]}
    
    df_cat_receita = pd.DataFrame(cat_receita)
    df_cat_despesa = pd.DataFrame(cat_despesas)
    df_cat_despesa.to_csv("df_cat_despesa.csv")
    df_cat_receita.to_csv("df_cat_receita.csv")
