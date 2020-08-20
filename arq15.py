import pandas as pd

df = pd.DataFrame({
                    'A': {0: 'a', 1: 'b', 2: 'c'},
                    'B': {0: 1, 1: 3, 2: 5},
                    'C': {0:2, 1:4, 2: 6}
})
print(df)

#combinação de valores de acordo com coluna de referencia e outra para o valor a ser combinado
comb_ab = pd.melt(df, id_vars= ['A'], value_vars=['B'])
print(comb_ab)

#combinação de AB e AC
comb_abc = pd.melt(df, id_vars= ['A'], value_vars=['B', 'C'])
print(comb_abc)

#renomeando as colunas
variaveis = pd.melt(df, id_vars= ['A'], value_vars=['B', 'C'], var_name= 'VarTeste', value_name= 'Nome do valor')
print(variaveis)