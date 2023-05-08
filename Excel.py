from itertools import count
import pyodbc
import pandas as pd


def Import():
    df = pd.read_excel()

    conexao_dw = ("Driver={SQL Server Native Client 11.0};"
                "Server=,1433;"
                "Database=;"
                ";"
                ")

    conexao_dw = pyodbc.connect(conexao_dw)
    cursor_dw = conexao_dw.cursor()
    print('conexão conluida')

    for i, empresaId in enumerate(df['empresaId']):
        obraId = df.loc[i,'obraId']
        identificador = df.loc[i,'identificador']
        nomeCliente = df.loc[i,'nomeCliente']
        cpfCnpj = df.loc[i,'cpfCnpj']
        data_venda = df.loc[i,'data_venda']


        script = '''insert into Lastro ([empresaId], [obraId], [identificador], [nomeCliente], [cpfCnpj], [data_venda]) values ('''
        dados = '\'' + empresaId + '\'' + ',\'' + obraId + '\'' + ',\'' + identificador + '\'' + ',\'' + nomeCliente + '\'' + ',\'' + str(cpfCnpj) + '\'' + ',\'' + str(data_venda) + '\'' +  ')' 

        query = script + dados
        cursor_dw.execute(query)
        cursor_dw.commit()
