import  pandas as pd
import numpy as np

#Criação dataframa dias
dias = pd.date_range(start= '20190101', periods=12)

Pessoa = ['George', 'Victor', 'Lucas']

np.random.choice(Pessoa)

Nome = []
Gasto = []

#Gera aleatoriamente pessoa e salva em nome
#Gera valor gasto aleatoriamente
for i in range(12):
    Nome.append(np.random.choice((Pessoa)))
    Gasto.append(np.round(np.random.rand() * 100, 2 ))

print(Nome)
print(Gasto)

#agrupando as informações em 1 dataframe
df = pd.DataFrame({'Dias': dias, 'Nome': Nome, 'Gasto': Gasto})
print(df)

#agrupamento usando pivot
gastos_dia = df.pivot(index= 'Dias', columns= 'Nome', values= 'Gasto' )
print(gastos_dia)

