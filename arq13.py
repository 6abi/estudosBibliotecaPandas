import pandas as pd

Carros = [7,4,3,2,8]
dias = pd.date_range('20200101', '20200101', periods= 5)

vendedor = ['Pedro', 'Wagner', 'Ana', 'Wagner', 'Pedro']

df = pd.DataFrame({'Vendas': Carros, 'Data': dias, 'Vendedor': vendedor})

print(df)

#com a pivot_table é possivel usar valor repeditos par ao index

#media dos valores
vendas_media = pd.pivot_table(df, index= 'Data', columns='Vendedor', values='Vendas')

#soma dos valores
vendas_soma = pd.pivot_table(df, index= 'Data', columns='Vendedor', values='Vendas', aggfunc= 'sum')


print(vendas_media)
print(vendas_soma)