import pandas as pd
import numpy as np



#geração de datas
datas = pd.date_range('20200101', periods= 10, freq = "D")

# criação de dataframe randomico
df = pd.DataFrame(np.random.randn(10,5), index = datas, columns = list("ABCDE"))

#primeiros 3 valores do dataset
print(df.head(3))

# 3 últimos valores do dataset
print(df.tail(3))

#indexes
print(df.index)

#colunas
print(df.columns)

#convertendo para lista
print(df.to_numpy())

#transposta (transformação de linha em coluna)
print(df.T)