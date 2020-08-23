import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#tamanho da figura
plt.rcParams['figure.figsize'] = (15,7)

df = pd.read_csv('../codigosComPandasEMatplotlib/titanic/train.csv')
print(df.head(5))
print(df.shape)
print(df.Age.describe)

#plotagem de histograma
df.Age.hist()
plt.xlabel('idade')
plt.ylabel('Frequência observada')
plt.savefig('../codigosComPandasEMatplotlib/titanic/hitograma.png', transparent = True)
plt.show()