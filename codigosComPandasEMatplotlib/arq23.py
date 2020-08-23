import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#tamanho da figura
plt.rcParams['figure.figsize'] = (20,7)

df = pd.read_csv('../codigosComPandasEMatplotlib/titanic/train.csv')
print(df.head(5))
print(df.shape)

#plotagem das idades em grafico de linha com matplotlib
# plt.plot(df.Age, '*-r')
# plt.title('Idade passageiros do Titanic')
# plt.xlabel('Passageiro', size = 18)
# plt.ylabel('Idade', size = 18)

#plotagem com a bibliteca panda
df.Age.plot()
plt.title('Idade passageiros do Titanic')
plt.xlabel('Passageiro', size = 18)
plt.ylabel('Idade', size = 18)

#plot de todos os dados
df.plot()
plt.savefig('../codigosComPandasEMatplotlib/titanic/linha.png', transparent = True)
plt.show()
