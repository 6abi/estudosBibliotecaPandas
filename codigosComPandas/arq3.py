import pandas as pd
import numpy as np


# criação de dataframe randomico
df = pd.DataFrame(np.random.randn(5,5), columns = list("ABCDE"), index=[0,1,2,3,4])


#Criação de dataframe com uso de chaves
df2 = pd.DataFrame({'A':7,
                    'B': pd.Timestamp('20200101'),
                    'C': np.array([2] * 4, dtype = 'int32'),
                    'D': np.array([3] * 4, dtype = 'int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"])},
                   index=[5,6,7,8]
                   )
# criação de dataframe randomico
df3 = pd.DataFrame(np.random.randn(5,5), columns = ["A","B","C","D","E"], index=[9,10,11,12,13])
print(df)
print(df2)
print(df3)

#concatenação dos dataframes
frames = [df,df2,df3]
framesCombinados = pd.concat(frames)
print(framesCombinados)

#agrupamento de frames
grupo = ( pd.concat([df,df2,df3], keys= ['f1','f2','f3']))
print(grupo)

#chamada pela chave
print(grupo.loc['f2'])

#concatenação com append
g2 = df.append(df2)
print(g2)