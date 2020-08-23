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
df2 = pd.DataFrame({"A":7,
                    'B': pd.Timestamp('20190101'),
                    'C': pd.Series(1, index=list(range(4)), dtype= 'float32'),
                    'D': np.array([3] * 4, dtype = 'int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'Python'
                    })
print(df2)

#criação de novas colunas em um dataframe existente
df['F'] = 1
print(df)
df['G'] = range(60)
print(df)
df['Produto'] = df['A'] * df['G']
print(df)
