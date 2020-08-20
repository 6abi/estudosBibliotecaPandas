import  pandas as pd
import numpy as np

datas = pd.date_range('20200101', periods= 600, freq='D')

df = pd.DataFrame(np.random.randn(600, 5), index= datas, columns=list("ABCDE"))
print(df.head(5))

#fatiamento de linhas e colunas na seleção de dados
x = df.iloc[2:4,0:2]
print(x)

#pegar indices especificos e não range
y = df.iloc[[1,5,7],[0,3]]
print(y)

#filtrando valores,valores maior do que 0 na coluna A
xx = df[df.A > 0]
print(xx)
