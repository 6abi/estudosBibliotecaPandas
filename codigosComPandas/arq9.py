import numpy as np
import pandas as pd
v = [22,45,7,9]

#pegar ultimo elemento
print(v[-1])

#lista de listas
arrays = [[1,1,2,2], ['red','blue','red','blue']]

#formando uma tupla com a biblioteca pandas - tabela
mult_index = pd.MultiIndex.from_arrays(arrays, names=('number','color'))
print(mult_index)
print(pd.MultiIndex)

