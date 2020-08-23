import  pandas as pd
import numpy as np

datas = pd.date_range('20200101', periods= 600, freq='D')

df = pd.DataFrame(np.random.randn(600, 5), index= datas, columns=list("ABCDE"))
print(df.head(5))

#todas as linhas de uma coluna
c = df['C']
print(c)

#pegar linha especifica, da 1 até 4
linha = df[1:5]
print(linha)

#pegando mais de 1 coluna
x = df.loc[:, ['B', 'C']]
print(x)

#pegar a partir das datas
y = df.loc['20200101': '20200320', ['A', 'E']]
print(y)