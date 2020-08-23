import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#tamanho da figura
plt.rcParams['figure.figsize'] = (15,7)

df = pd.read_csv('../codigosComPandasEMatplotlib/titanic/train.csv')
print(df.head(5))
print(df.shape)


#Scatter plot
#grafico de dispersão
plt.scatter(df.PassengerId, df.Age, marker= '+')
plt.show()