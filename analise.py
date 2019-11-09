# importa bibliotecas e funções
from functions import *

#importa dados em DF
df = import_dados()

#preprocessamento dos dados
df = data_prepro(df)

#print dos compilados dos das análises por média
print(df.groupby(['CNPJ',"year","month"])["lucro_g","lucro_e"].mean())