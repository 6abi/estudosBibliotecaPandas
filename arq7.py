import pandas as pd

#Cadastro da loja A
#Criação no dict com as informações
cadastro_a = {
                'Id': ['AA2930', 'BB4563', 'CC2139', 'DE2521', 'GT3462', 'HH1158'],
                'Nome': ['Victor', 'Amanda', 'Bruna', 'Carlos', 'Ricardo', 'Maria'],
                'Idade': [20,35,40,54,30,27],
                'CEP': ['00092-029', '11111-111', '22222-088', '00000-999', '88888-111', '77777-666']
            }

#criação do dataframe
cadastro_a = pd.DataFrame(cadastro_a, columns= [ 'Id', 'Nome', 'Idade', 'CEP'])

print(cadastro_a)

#Cadastro da loja B
#Criação no dict com as informações
cadastro_b = {
                'Id': ['CC9999', 'EF4488', 'DD9999', 'GT3462', 'HH1158'],
                'Nome': ['Marcos', 'Patricia', 'Ericka', 'Ricardo', 'Maria'],
                'Idade': [19,30,22,30,27],
                'CEP': ['00092-029', '11111-111', '11111-088', '88888-111', '77777-666']
            }

#criação do dataframe
cadastro_b = pd.DataFrame(cadastro_b, columns= [ 'Id', 'Nome', 'Idade', 'CEP'])

print(cadastro_b)

#Registro de compras de todas as unidades
compras = {
            'Id': ['AA2930', 'EF4488', 'CC2139', 'EF4488', 'CC9999', 'GT3462', 'AA2930', 'HH1158', 'HH1158'],
            'Data': ['2020-01-01','2020-01-30','2020-01-30','2020-02-01','2020-02-20','2020-03-15','2020-03-25','2020-04-01','2020-01-10'],
            'Valor': [200,100,40,150,300,25,50,500, 250]
        }

compras = pd.DataFrame(compras, columns= [ 'Id', 'Data', 'Valor'])
print(compras)


#função merge
#pd.merge(t_esquerda, t_direita, on = 'coluna_coincidente", how = "left|right|inner|outer")

#indicar onde contem o dado, outer e indicator
juncao = pd.merge(cadastro_a, cadastro_b, how='outer', on=['Id'], indicator=True)
print(juncao)





