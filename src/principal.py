import os # pacote para pegar o diretorio atual
from pathlib import Path # pacote para pegar o diretorio pai do diretorio atual
from dotenv import load_dotenv #instalar o pacote python-dotenv
load_dotenv()# Para ler as variaveis do arquivo .env
from meusPacotes.emailYahoo import enviar_email
from meusPacotes.meuDataframe import tratar_df
from data.entrada import dict_fornecedor #dados de entrada

def main():
    # criar uma funcao para transformar o dicionario em data e acrescentar as colunas como se pede
    df = tratar_df(dict_fornecedor)
    # 2 fornecedores ficaram faltando na lista, criar um dicionario com esse dois fornecedores e seus respectivos nomes e vendas (pode usar a imaginaçao).
    # criar um dataframe usando a mesma funcao acima que foi criada p tratar df.
    # acrecentar no final do df original esse df complementar com os dois fornecedores.
    # crie uma pasta "files"e grave em formato excel (.xlsx)
    BASE_DIR = str(Path(os.path.dirname(__file__)).parent) #diretorio base do programa
    file = BASE_DIR + '/files/evento.xlsx'
    df.to_excel(file)
    # filtre os 3 maiores vendedores de comida salgada mais a primeira de doce e mande email para eles congratulando-os
    doces = df.loc[df.tipo=='doces',:]
    salgados = df.loc[df.tipo=='salgados',:]
    doce1 = doces.sort_values(['vendas'], ascending=False).reset_index(drop=True).loc[0]
    salgado3 = salgados.sort_values(['vendas'], ascending=False).reset_index(drop=True).loc[0:2]
    # cria uma lista com os emails
    emails = [doce1.email]
    for row in salgado3.itertuples():
        emails += [row.email]
    # crie uma função que mande esses 4 emails de forma automática
    for email in emails:
        destinatario = email
        assunto = 'teste aula'
        mensagem = 'teste de envio de email usando chatGPT'
        usuario = os.environ.get("YAHOO_USER") #pega o usuario do arquivo .env
        senha = os.environ.get("YAHOO_PASSWORD") #pega a senha do arquivo .env
        enviar_email(usuario, senha, destinatario, assunto, mensagem)

if __name__ == '__main__':
    main()


