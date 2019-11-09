#imports
import os
import pandas as pd
import time

#variáveis
directory = "input/Pedido 1 LAI ANP"
def import_dados():
    print("begin import dados. Header is:  \n")
    dfs = list()
    for file in os.listdir(directory):
        if file.endswith(".xlsx"):

            # print(os.path.join(directory, file))
            dfs.append(pd.read_excel(os.path.join(directory, file),usecols = ['BAIRRO', 'BANDEIRA', 'CEP', 'CNPJ', 'DISTRIBUIDORA ETANOL', 'DISTRIBUIDORA GASOLINA', 'MODALIDADE DE COMPRA ETANOL', 'MODALIDADE DE COMPRA GASOLINA',  'PREÇO COMPRA ETANOL (R$/LITRO)', 'PREÇO COMPRA GASOLINA (R$/LITRO)','PREÇO VENDA ETANOL (R$/LITRO)', 'PREÇO VENDA GASOLINA (R$/LITRO)',  'RAZÃO SOCIAL', 'SEMANA INICIO'],infer_datetime_format=True))
            continue
        else:
            continue
    result = pd.concat(dfs,ignore_index=True,sort=True)
    print(list(result))
    print("end import dados \n")
    result["lucro_g"] = 0
    return result

def data_prepro(df):
    df['year'] = pd.DatetimeIndex(df['SEMANA INICIO']).year
    df['month'] = pd.DatetimeIndex(df['SEMANA INICIO']).month

    lista = df.CNPJ.unique()
    print("observações totais: " + str(len(df)))

    combustível_venda = ["PREÇO VENDA GASOLINA (R$/LITRO)", 'PREÇO VENDA ETANOL (R$/LITRO)']
    combustível_compra = ['PREÇO COMPRA GASOLINA (R$/LITRO)', 'PREÇO COMPRA ETANOL (R$/LITRO)']
    indexcombustível = ["lucro_g", "lucro_e"]

    for empresa in lista:

        dftemp = df[df["CNPJ"] == empresa]
        dftemp = dftemp.sort_values(by=['year', 'month'])
        dftemp = dftemp.interpolate(method="linear")
        # dftemp = dftemp.interpolate( limit_direction='backward')
        # dftemp = dftemp.fillna(method='ffill',limit = 4)
        # dftemp = dftemp.fillna(method='bfill',limit = 4)

        for a, b, c in zip(combustível_venda, combustível_compra, indexcombustível):
            dftemp[c] = dftemp[a] - dftemp[b]
            lista = dftemp.index.tolist()
            for i in lista:
                df.loc[df.index == i, c] = dftemp.at[i, c]

    df = df.dropna(subset=indexcombustível)

    print("observações com valor de lucro :" + str(len(df)))
    return df
