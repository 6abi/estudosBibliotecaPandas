import pandas as pd
import numpy as np

#Criação de dataframe com uso de chaves
df2 = pd.DataFrame({"A":1,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype= 'float32'),
                    'D': np.array([3] * 4, dtype = 'int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'Python',
                    'G': [2,2,4,4],
                    'H': [np.nan,2,4,np.nan]
                    })
print(df2)

#dados unicos no dataframe
unicos = df2.nunique()
print(unicos)

#removendo duplicatas
duplicados = df2.drop_duplicates(subset='G')
print(duplicados)