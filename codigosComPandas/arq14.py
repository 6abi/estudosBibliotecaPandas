import pandas as pd

df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

print(df.head(4))
print(df.shape)

#empilhar os dados, "agrupamento" em pilha por indice (stack)
stack_df = df.stack()
print(stack_df)

#retornar ao estado anterior - desempilhar
udf = stack_df.unstack()
print(udf.head(3))



