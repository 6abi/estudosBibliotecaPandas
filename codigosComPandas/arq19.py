import pandas as pd
import numpy as np

#geração de serie temporal
series = pd.Series([7,4,2,np.nan,6,9, ])
print(series)
print(series.describe())
print(type(series))

#geração de datas
datas = pd.date_range('20200101', periods= 60, freq = "D")
print(datas)

# criação de dataframe randomico
df = pd.DataFrame(np.random.randn(60,5), index = datas, columns = list("ABCDE"))
print(df)
print(df.shape)

#Criação de dataframe com uso de chaves
df2 = pd.DataFrame({"A":1,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype= 'float32'),
                    'D': np.array([3] * 4, dtype = 'int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'Python'
                    })
print(df2)

#visualição do tipo de dados
print(df2.dtypes)

#somente para dados numericos - estatistica descritiva
print(df2.describe())

#novo dataframe com reindexão e adição de coluna nova
df1 = df.reindex(index=datas[0:4], columns = list(df.columns) + ['F'])
print(df1)

#adiciona valor nas linhas 1 e 2 coluna F
df1.loc[datas[0]:datas[1], 'F'] = 77
print(df1)


df1.describe()

df['G'] = df.B[df.B > 0]
print(df.head(3))

df3 = df.copy()

#exclui linha que tenha algum dado faltante
df4 = df.copy().dropna()
print(df4)

#substituição na coluna G de valor faltante por uma media
#fillna(value = valor_da_substituição)
media = df3.G.fillna(np.mean(df3.B))
print(media)




