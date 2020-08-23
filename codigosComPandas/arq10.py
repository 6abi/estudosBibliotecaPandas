import numpy as np
import pandas as pd
v = [22,45,7,9]

#pegar ultimo elemento
print(v[-1])

#lista de listas
numbers= [0,1,2,3]
colors = ['red','purple','grey','blue']

#formando uma tupla com a biblioteca pandas - tabela
mult_index = pd.MultiIndex.from_product([numbers, colors],
                                        names= ['number', 'color'])
print(mult_index)
print(pd.MultiIndex)

