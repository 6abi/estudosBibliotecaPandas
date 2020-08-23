import pandas as pd
import  numpy as np

#criação do dataframe com string e numeros
df = pd.DataFrame({
                    'A': ['verdadeiro','falso','verdadeiro','falso',
                         'verdadeiro','falso','verdadeiro','falso'],
                    'B': ['um','um','dois', 'tres', 'dois', 'dois', 'um', 'tres'],
                    'C': np.random.randn(8),
                    'D': np.random.randn(8)
                })
print(df)

#agrupamento pela coluna A e somando
soma_a = df.groupby(['A']).sum()
print(soma_a)

#media pela coluna A e somando
media = df.groupby(['A']).mean()
print(media)

#media pela coluna B e somando
soma_b = df.groupby(['B']).sum()
print(soma_b)

#agrupamento por 2 ou + colunas
soma_ab = df.groupby(['A', 'B']).sum()
print(soma_ab)
