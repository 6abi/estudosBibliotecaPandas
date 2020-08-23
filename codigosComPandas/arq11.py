import pandas as pd
import numpy as np

#criação datas
datas = pd.date_range('20200101', periods=6)

#criação data frame dados aleatorios
df = pd.DataFrame(np.random.randn(6, 4), index= datas, columns=['Var_A', 'Var_B','Var_C', 'Var_D'])

print(df)

#transposta - linha se torna coluna e coluna se torna linha
dft = df.T
print(dft)

#atributo shape
print(df.shape)
print(dft.shape)

#extraindo valores do conjunto de dados
v = dft.values
print(v)

#qtde de dados no dataframe
qtd = np.size(dft.values)
print(qtd)

#reformatação dos dados
new_v = v.reshape((2,12))
print(new_v)