import pandas as pd
import re

def tratar_df(dict_fornecedor):
    # Trasforme o dicionario dict_fornecedor em um DataFrame
    df = pd.DataFrame.from_dict(dict_fornecedor, orient='index')
    # Crie um coluna "email" e insera o email do fornecedor
    # coloque o nome em letra minuscula
    # troque o espaco por "_"
    # acrescente "@gmail.com"
    lst_nomes = df['nome'].values
    lst_email = []
    for nome in lst_nomes:
        nome = nome.lower()
        nome = nome.replace(" ", "_")
        nome = nome + "@gmail.com"
        lst_email += [nome]
    df['email'] = lst_email
    # crie uma coluna com o valor de 50% das vendas com o nome repasse
    # esse valor é o valor a ser repassado pelos organizadores ao fornecedor
    df['repasse'] = df['vendas'] * 0.5
    # crie uma coluna com o nome "tipo"
    # essa coluna tem a funcao de classificar quais fornecedores vendem sobremesas e doces apenas
    # classique como "doces" os fornecedores que tem no nome "bolo", "doceria" ou "brigadeiro"
    pattern = 'bolo|doceria|brigadeiro'
    df['tipo'] = df['nome'].apply(lambda x: 'doces' if bool(re.search(pattern, x, re.IGNORECASE)) else 'salgados')
    return df




    