from time import sleep
import pandas as pd 

venda = {'data' : ['15/02/2021', '16/02/2021'],
'valor':[500, 300],
'produto': ['feijao', 'arroz'],
'qtde' : [50, 70],}

vendas_df = pd.DataFrame(venda)

print(vendas_df)
print()
print()



vendas_df = pd.read_excel('/storage/emulated/0/Download/Vendas - Dez.xlsx')

print(vendas_df)

print()


print(vendas_df.head())



print(vendas_df.shape)
print()

print(vendas_df.describe())


'''se quiser passar mais de um valor coloca mais um colchetes e depois passa o id do produto'''
produtos = vendas_df[['Produto', 'ID Loja']]
print(produtos)

print(vendas_df.loc[1:3])


vendas_df_NorteShopping =vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']]


print(vendas_df_NorteShopping)

#print(vendas_df.loc[linha, coluna])

print(vendas_df.loc[1, 'Produto'])




vendas_df['imposto'] = 0
vendas_df.loc[:, 'imposto'] = 0

'''ambos codigos acima est˜ao corretos so escolher qual ´e o melhor para a situaç˜ao'''

print(vendas_df)


vendas_df_dz = pd.read_excel('/storage/emulated/0/Download/Vendas - Dez.xlsx')

print(vendas_df_dz)

vendas_df = vendas_df.append(vendas_df_dz)



'''excluir linha'''

vendas_df = vendas_df.drop('imposto', axis = 1)
print(vendas_df)

'''linhas e colunas vazias'''

vendas_df = vendas_df.dropna(how ='all', axis = 1)


''''deletar linhas com apenas alguns valores vazios'''

vendas_df = vendas_df.dropna()


'''prencher linhas vazias'''







''' Calcular indicadores'''
'''value_counts'''
'''groupby'''


#Value_counts
transaçoes_loja = vendas_df['ID Loja'].value_counts()

print(transaçoes_loja)


#groupby

faturamento_prod = vendas_df[['Produto','Valor Final']].groupby('Produto').sum()


print(faturamento_prod)



'''mesclar 2 dataframes'''


gerentes_df = pd.read_excel('arquivo do gerentes')

vendas_df = vendas_df.merge(gerentes_df)