#imports
import os
import pandas as pd

#variáveis
directory = "input/Pedido 1 LAI ANP"
def import_dados():
    print("begin import dados. Header is:  \n")
    dfs = list()
    for file in os.listdir(directory):
        if file.endswith(".xlsx"):

            # print(os.path.join(directory, file))
            dfs.append(pd.read_excel(os.path.join(directory, file)))
            continue
        else:
            continue
    result = pd.concat(dfs,ignore_index=True,sort=True)
    header = list(result)
    print(header)
    print("end import dados \n")
    return result
