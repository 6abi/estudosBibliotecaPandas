import numpy as np
import pandas as pd

df = pd.DataFrame({'col1': ['A','A','B', np.nan, 'D', 'C'],
                    'col2': [2,1,9,8,7,4],
                    'col3': [0,1,9,4,2,3]
                   })

print(df)

#ordenação de valores
ordena = df.sort_values(by= ['col3', 'col2'], ascending=False)
print(ordena)